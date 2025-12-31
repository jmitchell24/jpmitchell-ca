import requests
import time
import re
from urllib.parse import quote
import sys
import argparse
import os

def extract_urls_from_markdown(filename):
    """Extract all URLs from a markdown file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        urls = set()
        
        # Pattern 1: Markdown links [text](url)
        markdown_links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
        for text, url in markdown_links:
            if url.startswith('http'):
                urls.add(url)
        
        # Pattern 2: Plain URLs (http:// or https://)
        plain_urls = re.findall(r'https?://[^\s\)\]<>"]+', content)
        urls.update(plain_urls)
        
        # Pattern 3: Reference-style links [text][ref] and [ref]: url
        ref_definitions = re.findall(r'^\[([^\]]+)\]:\s*(https?://[^\s]+)', content, re.MULTILINE)
        for ref, url in ref_definitions:
            urls.add(url)
        
        return sorted(list(urls))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def check_archive_snapshot(url):
    """Check if a URL has a snapshot on archive.org."""
    api_url = f"https://archive.org/wayback/available?url={quote(url)}"
    
    try:
        response = requests.get(api_url, timeout=10)
        data = response.json()
        
        if data.get('archived_snapshots') and data['archived_snapshots'].get('closest'):
            snapshot_url = data['archived_snapshots']['closest']['url']
            return snapshot_url, True
        return None, False
    except Exception as e:
        print(f"Error checking snapshot for {url}: {e}")
        return None, False

def create_archive_snapshot(url):
    """Request archive.org to create a new snapshot."""
    save_url = f"https://web.archive.org/save/{url}"
    
    try:
        response = requests.get(save_url, timeout=30)
        
        if response.status_code == 200:
            # Extract the snapshot URL from the response
            snapshot_url = response.url
            return snapshot_url, True
        return None, False
    except Exception as e:
        print(f"Error creating snapshot for {url}: {e}")
        return None, False

def process_markdown_urls(input_file, output_file):
    """Process all URLs from markdown file and generate a report."""
    urls = extract_urls_from_markdown(input_file)
    
    if not urls:
        print("No URLs found in the markdown file.")
        sys.exit(1)
    
    results = []
    
    print(f"Found {len(urls)} unique URLs in markdown file\n")
    
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] Processing: {url}")
        
        # Check for existing snapshot
        snapshot_url, exists = check_archive_snapshot(url)
        
        if exists:
            print(f"  ✓ Found existing snapshot")
            results.append({
                'original_url': url,
                'snapshot_url': snapshot_url,
                'status': 'existing'
            })
        else:
            print(f"  ⟳ No snapshot found. Creating new one...")
            snapshot_url, created = create_archive_snapshot(url)
            
            if created:
                print(f"  ✓ Created new snapshot")
                results.append({
                    'original_url': url,
                    'snapshot_url': snapshot_url,
                    'status': 'created'
                })
            else:
                print(f"  ✗ Failed to create snapshot")
                results.append({
                    'original_url': url,
                    'snapshot_url': 'N/A',
                    'status': 'failed'
                })
        
        # Be respectful of archive.org servers
        time.sleep(2)
        print()
    
    # Write results to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Archive.org Snapshot Results\n")
        f.write("=" * 80 + "\n\n")
        
        for result in results:
            f.write(f"Original URL: {result['original_url']}\n")
            f.write(f"Snapshot URL: {result['snapshot_url']}\n")
            f.write(f"Status: {result['status']}\n")
            f.write("-" * 80 + "\n")
        
        # Also create a simple list of snapshot URLs
        f.write("\n\nSnapshot URLs Only:\n")
        f.write("=" * 80 + "\n")
        for result in results:
            if result['snapshot_url'] != 'N/A':
                f.write(f"{result['snapshot_url']}\n")
    
    print(f"\n✓ Results saved to '{output_file}'")
    print(f"\nSummary:")
    print(f"  Total URLs: {len(results)}")
    print(f"  Existing snapshots: {sum(1 for r in results if r['status'] == 'existing')}")
    print(f"  New snapshots: {sum(1 for r in results if r['status'] == 'created')}")
    print(f"  Failed: {sum(1 for r in results if r['status'] == 'failed')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Check and create Archive.org snapshots for URLs in a markdown file'
    )
    parser.add_argument(
        'input_file',
        help='Path to the markdown file containing URLs'
    )
    parser.add_argument(
        '-o', '--output',
        default='archive_snapshots.txt',
        help='Output file for results (default: archive_snapshots.txt)'
    )
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.isfile(args.input_file):
        print(f"Error: File '{args.input_file}' not found.")
        sys.exit(1)
    
    print("Archive.org Snapshot Checker for Markdown")
    print("=" * 80)
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output}")
    print()
    
    process_markdown_urls(args.input_file, args.output)
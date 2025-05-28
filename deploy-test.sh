#!/bin/bash

# Configuration
LOCAL_DIR="public/"
SSH_HOST="me.dmz"  # SSH hostname from ~/.ssh/config
REMOTE_DIR="/var/www/html/"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if local directory exists
if [ ! -d "$LOCAL_DIR" ]; then
    print_error "Local directory '$LOCAL_DIR' does not exist!"
    exit 1
fi

print_status "Starting deployment..."
print_status "Local directory: $LOCAL_DIR"
print_status "Remote host: $SSH_HOST:$REMOTE_DIR"

# Rsync command with options:
# -a: archive mode (preserves permissions, timestamps, etc.)
# -v: verbose output
# -z: compress data during transfer
# --delete: delete files on remote that don't exist locally
# --exclude: exclude common files that shouldn't be deployed
rsync -avz --delete \
    "$LOCAL_DIR" \
    "$SSH_HOST:$REMOTE_DIR"

# Check if rsync was successful
if [ $? -eq 0 ]; then
    print_status "Deployment completed successfully!"
    
    # Optional: restart nginx (uncomment if needed)
    # print_status "Restarting nginx..."
    # ssh "$SSH_HOST" "sudo systemctl restart nginx"
    
else
    print_error "Deployment failed!"
    exit 1
fi
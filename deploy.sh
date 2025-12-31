#!/bin/bash
# Get Commit Message from Arg or use Default
COMMIT_MSG="${1:-deploy}"
BRANCH_NAME="${2:-main}"
DATE=$(date +%Y-%m-%d)
FULL_COMMIT_MSG="[ $DATE ] $COMMIT_MSG"

# Validate branch name
if [ "$BRANCH_NAME" != "main" ] && [ "$BRANCH_NAME" != "testing" ]; then
    echo "Error: Branch must be 'main' or 'testing'. Got: '$BRANCH_NAME'"
    exit 1
fi

# Build Site 
rm -rf public  

# Use --drafts flag if branch is 'testing'
if [ "$BRANCH_NAME" = "testing" ]; then
    zola build --drafts
else
    zola build
fi

cp README.md public/README.md

# Enter /public Directory
cd public

# Clone Github Repo, Keeping only the .git Directory 
if git clone -b $BRANCH_NAME https://github.com/jmitchell24/ca-lzon.git .git-tmp 2>/dev/null; then
    mv .git-tmp/.git .
    rm -rf .git-tmp
# Otherwise, create new Repo 
else
    git init
    git remote add origin https://github.com/jmitchell24/ca-lzon.git
fi

# Commit Everything in Directory to specified branch 
git add -A
git commit -am "$FULL_COMMIT_MSG"
git branch -M $BRANCH_NAME

# Push to Github Repo
git push -u origin $BRANCH_NAME

# Leave Directory 
cd -
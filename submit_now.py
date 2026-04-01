#!/usr/bin/env python3
"""
Complete Submission - Adds files, commits, and pushes to CURRENT BRANCH
IMPORTANT: You must create and checkout your branch BEFORE running this!
Run: git checkout -b submission/yourname-timestamp
Then run: python submit_now.py
"""

import os
import subprocess
import sys
import json
import time

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)

print("=" * 60)
print("🥧 Pi Value World - Complete Submission")
print("=" * 60)

# Find JSON files in root directory first
root_json_files = [f for f in os.listdir('.') 
                   if f.startswith('pi_result_') and f.endswith('.json')]

# Also check verification_list directory
verification_json_files = [f for f in os.listdir('verification_list') 
                           if f.startswith('pi_result_') and f.endswith('.json')]

# Combine both lists
json_files = root_json_files + verification_json_files

if not json_files:
    print("\n❌ No submission files found!")
    print("\n💡 Did you forget to run the calculation script?")
    print("   Run: python src/piclalculation.py")
    print("\n   OR did you forget to move your file to verification_list/ ?")
    print("   Copy your pi_result_*.json to verification_list/")
    sys.exit(1)

print(f"\n✅ Found {len(json_files)} file(s)")

# If files are in root, offer to move them
if root_json_files:
    print(f"\n📂 Found {len(root_json_files)} file(s) in root directory")
    for filename in root_json_files:
        print(f"   - {filename}")
    
    # Auto-move to verification_list
    import shutil
    for filename in root_json_files:
        src = os.path.join('.', filename)
        dst = os.path.join('verification_list', filename)
        shutil.move(src, dst)
        print(f"   ✅ Moved: {filename} → verification_list/")
    
    print("\n💡 Files moved to verification_list/ automatically!")

# Read username
with open(os.path.join('verification_list', json_files[0]), 'r') as f:
    data = json.load(f)
    username = data.get('github_username', 'unknown')

print(f"👤 Username: @{username}")

# Check current branch
print("\n📋 Step 1/4: Checking current branch...")
success, current_branch = run_command('git rev-parse --abbrev-ref HEAD')
if not success:
    print(f"❌ Failed to get current branch: {current_branch}")
    sys.exit(1)

current_branch = current_branch.strip()
print(f"✅ Current branch: {current_branch}")

# Check remote URL to verify it's a fork
print("\n🔍 Checking repository remote...")
success, remote_url = run_command('git remote get-url origin')
if success:
    remote_url = remote_url.strip()
    if 'harinandsindukumar/pivalue.world' in remote_url:
        print("\n⚠️  WARNING: You're trying to push to the ORIGINAL repo!")
        print("\n❌ This won't work - you don't have permission to push here.")
        print("\n💡 You need to:")
        print("   1. Fork the repository on GitHub first")
        print("   2. Clone YOUR fork (not the original)")
        print("   3. Then run this script")
        print("\n📋 Correct workflow:")
        print("   # Go to: https://github.com/harinandsindukumar/pivalue.world")
        print("   # Click 'Fork' button")
        print("   # Then clone YOUR fork:")
        print(f"   git clone https://github.com/YOUR_USERNAME/pivalue.world.git")
        print(f"   cd pivalue.world")
        print(f"   git checkout -b {current_branch}")
        print(f"   python submit_now.py")
        sys.exit(1)
    else:
        print(f"✅ Remote URL looks correct: {remote_url}")
else:
    print("⚠️  Could not check remote URL")

if current_branch == 'main':
    print("\n⚠️  WARNING: You're on main branch!")
    print("You should create a new branch first:")
    print(f"   git checkout -b submission/{username}-{int(time.time())}")
    print("\nThen run this script again.")
    sys.exit(1)

# Step 2: Add files
print(f"\n📝 Step 2/4: Adding files to {current_branch}...")
success, output = run_command("git add -A verification_list/")
if not success:
    print(f"❌ Failed: {output}")
    sys.exit(1)

# Verify files staged
success, staged = run_command("git diff --cached --name-only")
if not staged.strip():
    print("\n⚠️  No files to add!")
    
    # Check if files were already committed
    success, unstaged = run_command("git status --porcelain verification_list/")
    if unstaged.strip():
        print("\n📂 Files found but not staged!")
        print("\n💡 Solution: Reset and try again")
        print("   Run these commands:")
        print("   git reset")
        print("   python submit_now.py")
        sys.exit(1)
    
    # Check if already committed in this branch
    success, log = run_command(f"git log {current_branch} --oneline -1")
    if log.strip():
        print("\n✅ Files already committed in this branch!")
        print(f"\n📋 Current branch '{current_branch}' already has your submission.")
        print("\n💡 Next step: Just push to GitHub")
        print("   Run: git push -u origin", current_branch)
        print("\n   OR create a new branch with a fresh timestamp:")
        print("   git checkout main")
        print("   git checkout -b submission/YOUR_USERNAME-newtimestamp")
        print("   Then run this script again")
        sys.exit(1)
    
    print("\n💡 Possible reasons:")
    print("   1. File already committed in this branch")
    print("   2. File not in verification_list/ directory")
    print("   3. Git tracking issue")
    print("\n✅ Quick fix:")
    print("   git status  (check what's changed)")
    print("   git reset   (unstage if needed)")
    print("   Then run this script again")
    sys.exit(1)

print(f"✅ Added {len(staged.strip().split())} file(s)")

# Step 3: Commit
print("\n💾 Step 3/4: Committing...")
commit_msg = f"feat: add Pi Value World submission for {username}"
success, output = run_command(f'git commit -m "{commit_msg}"')
if not success:
    print(f"❌ Failed: {output}")
    sys.exit(1)
print("✅ Committed successfully!")

# Step 4: Push
print("\n🚀 Step 4/4: Pushing to GitHub...")
success, output = run_command(f'git push -u origin {current_branch}')
if not success:
    print(f"❌ Failed: {output}")
    print(f"\nManual fix: git push -u origin {current_branch}")
    sys.exit(1)
print("✅ Pushed successfully!")

print("\n" + "=" * 60)
print("🎉 SUCCESS!")
print("=" * 60)
print(f"\n✨ Your code is on branch: {current_branch}")
print("\n📋 Create Pull Request:")
print("1. GitHub will show link automatically")
print("2. Or go to: https://github.com/harinandsindukumar/pivalue.world")
print("3. Click 'Pull requests' → 'New pull request'")
print(f"4. Select: base: main ← compare: {current_branch}")
print(f"5. Title: feat: add submission for {username}")
print("\n💡 Include your codes from the JSON file!")
print("=" * 60)

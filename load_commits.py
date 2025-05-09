#!/usr/bin/env python3

import json
import subprocess
import os
import argparse

def load_commits_content(file_path='commits_content.json'):
    with open(file_path, 'r', encoding='utf-8') as f:
        commits_content = json.load(f)
    return commits_content

def apply_commit(commit):
    commit_message = commit['commit_message']
    
    print(f"Applying commit: {commit_message}")
    
    # Apply added files
    for file_path, content in commit['added_files'].items():
        print(f"  Adding file: {file_path}")
        dirname = os.path.dirname(file_path)
        if dirname:  # Only create directory if dirname is not empty
            os.makedirs(dirname, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        subprocess.run(['git', 'add', file_path], check=True)
    
    # Apply modified files
    for file_path, content in commit['modified_files'].items():
        print(f"  Modifying file: {file_path}")
        dirname = os.path.dirname(file_path)
        if dirname:  # Only create directory if dirname is not empty
            os.makedirs(dirname, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        subprocess.run(['git', 'add', file_path], check=True)
    
    # Apply deleted files
    for file_path in commit.get('deleted_files', []):
        print(f"  Deleting file: {file_path}")
        if os.path.exists(file_path):
            subprocess.run(['git', 'rm', file_path], check=True)

    # Commit the changes
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    print(f"Commit applied: {commit_message}\n")

def main():
    parser = argparse.ArgumentParser(description="Load and apply commits from a JSON file.")
    parser.add_argument('file_path', type=str, help='Path to the JSON file containing commits')
    args = parser.parse_args()

    commits_content = load_commits_content(args.file_path)
    
    for commit in commits_content:
        apply_commit(commit)

if __name__ == "__main__":
    main()
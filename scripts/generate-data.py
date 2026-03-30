#!/usr/bin/env python3
"""
leetcode-algorithms 레포에서 풀이 데이터를 가져와 solutions.json 생성.
GitHub Actions에서 실행됨.
"""
import json
import os
import re
import sys
from pathlib import Path

def detect_language(filename):
    ext_map = {
        '.kt': 'Kotlin', '.java': 'Java', '.py': 'Python',
        '.js': 'JavaScript', '.ts': 'TypeScript', '.cpp': 'C++',
        '.c': 'C', '.go': 'Go', '.rs': 'Rust', '.swift': 'Swift'
    }
    ext = Path(filename).suffix.lower()
    return ext_map.get(ext, 'Unknown')

def extract_complexity(code):
    """Try to extract time/space complexity from comments."""
    time_re = re.search(r'[Tt]ime\s*[Cc]omplexity\s*[:=]\s*(O\([^)]+\))', code)
    space_re = re.search(r'[Ss]pace\s*[Cc]omplexity\s*[:=]\s*(O\([^)]+\))', code)
    return (
        time_re.group(1) if time_re else None,
        space_re.group(1) if space_re else None
    )

def extract_author(code, filename):
    """Try to extract author from comments, fallback to filename pattern."""
    author_re = re.search(r'@author\s+(\S+)', code)
    if author_re:
        return author_re.group(1)
    # Check for author in filename like "0001-two-sum-성규.kt"
    parts = Path(filename).stem.split('-')
    # Default author from git blame could be added later
    return None

def get_git_authors(data_dir):
    """Get file → author mapping from git log."""
    import subprocess
    authors = {}
    try:
        result = subprocess.run(
            ['git', 'log', '--pretty=format:%an', '--name-only', '--diff-filter=A'],
            cwd=data_dir, capture_output=True, text=True, timeout=30
        )
        lines = result.stdout.strip().split('\n')
        current_author = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if '/' not in line and '.' not in line:
                current_author = line
            elif current_author:
                authors[line] = current_author
    except Exception as e:
        print(f"Git log failed: {e}")
    return authors

def main():
    data_dir = sys.argv[1] if len(sys.argv) > 1 else './leetcode-data'
    output_dir = sys.argv[2] if len(sys.argv) > 2 else './data'

    os.makedirs(output_dir, exist_ok=True)
    git_authors = get_git_authors(data_dir)
    solutions = {}

    if not os.path.isdir(data_dir):
        print(f"Data dir not found: {data_dir}")
        json.dump({}, open(f"{output_dir}/solutions.json", 'w'))
        return

    for folder in sorted(os.listdir(data_dir)):
        folder_path = os.path.join(data_dir, folder)
        if not os.path.isdir(folder_path) or folder.startswith('.'):
            continue

        entry = {
            "folder": folder,
            "description": "",
            "solutions": []
        }

        for fname in sorted(os.listdir(folder_path)):
            fpath = os.path.join(folder_path, fname)
            if not os.path.isfile(fpath):
                continue

            if fname == 'README.md':
                with open(fpath, 'r', encoding='utf-8') as f:
                    entry["description"] = f.read()[:2000]  # Truncate
                continue

            lang = detect_language(fname)
            if lang == 'Unknown':
                continue

            with open(fpath, 'r', encoding='utf-8') as f:
                code = f.read()

            time_c, space_c = extract_complexity(code)
            git_key = f"{folder}/{fname}"
            author = extract_author(code, fname) or git_authors.get(git_key, "anonymous")

            entry["solutions"].append({
                "filename": fname,
                "author": author,
                "language": lang,
                "code": code,
                "timeComplexity": time_c,
                "spaceComplexity": space_c,
                "notes": None
            })

        if entry["solutions"] or entry["description"]:
            solutions[folder] = entry

    with open(f"{output_dir}/solutions.json", 'w', encoding='utf-8') as f:
        json.dump(solutions, f, ensure_ascii=False, indent=2)

    total = sum(len(s["solutions"]) for s in solutions.values())
    print(f"Generated {len(solutions)} problems, {total} solutions")

if __name__ == '__main__':
    main()

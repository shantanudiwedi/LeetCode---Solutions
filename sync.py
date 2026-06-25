#!/usr/bin/env python3
import os
import requests
import base64
import json
import sys
from datetime import datetime

LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION", "")
GITHUB_TOKEN     = os.environ.get("GITHUB_TOKEN", "")
GITHUB_REPO      = os.environ.get("GITHUB_REPO", "")

DIFFICULTY_FOLDER = {"Easy": "Easy", "Medium": "Medium", "Hard": "Hard"}
EXTENSIONS = {
    "python3": "py", "python": "py", "java": "java",
    "cpp": "cpp", "c": "c", "javascript": "js",
    "typescript": "ts", "go": "go", "rust": "rs",
}

def get_latest_accepted():
    print("Fetching latest accepted submission...")
    headers = {
        "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}",
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0",
    }
    query = {
        "query": """
        query recentAcSubmissions {
            recentAcSubmissionList(username: "", limit: 5) {
                id
                title
                titleSlug
                timestamp
                lang
            }
        }
        """,
        "variables": {}
    }
    r = requests.post(
        "https://leetcode.com/graphql",
        json=query,
        headers=headers,
        timeout=15
    )
    r.raise_for_status()
    data = r.json()
    submissions = data["data"]["recentAcSubmissionList"]
    if not submissions:
        print("No accepted submissions found!")
        sys.exit(1)
    return submissions[0], headers

def get_submission_code(submission_id, headers):
    print(f"Fetching code for submission {submission_id}...")
    r = requests.get(
        f"https://leetcode.com/api/submissions/{submission_id}/",
        headers=headers,
        timeout=15
    )
    r.raise_for_status()
    return r.json().get("code", "")

def get_difficulty(title_slug, headers):
    print(f"Fetching difficulty for {title_slug}...")
    query = {
        "query": """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                difficulty
            }
        }
        """,
        "variables": {"titleSlug": title_slug}
    }
    r = requests.post(
        "https://leetcode.com/graphql",
        json=query,
        headers=headers,
        timeout=15
    )
    r.raise_for_status()
    q = r.json()["data"]["question"]
    return q["questionId"], q["difficulty"]

def push_to_github(folder, filename, content, commit_msg):
    print(f"Pushing {folder}/{filename} to GitHub...")
    api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{folder}/{filename}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }
    existing = requests.get(api_url, headers=headers, timeout=15)
    sha = existing.json().get("sha") if existing.status_code == 200 else None

    payload = {
        "message": commit_msg,
        "content": base64.b64encode(content.encode()).decode(),
    }
    if sha:
        payload["sha"] = sha

    r = requests.put(api_url, headers=headers, json=payload, timeout=15)
    r.raise_for_status()
    print(f"Uploaded: {r.json()['content']['html_url']}")

def main():
    if not LEETCODE_SESSION:
        print("ERROR: LEETCODE_SESSION not set"); sys.exit(1)
    if not GITHUB_TOKEN:
        print("ERROR: GITHUB_TOKEN not set"); sys.exit(1)
    if not GITHUB_REPO:
        print("ERROR: GITHUB_REPO not set"); sys.exit(1)

    submission, headers = get_latest_accepted()

    sub_id    = submission["id"]
    title     = submission["title"]
    slug      = submission["titleSlug"]
    lang      = submission["lang"]
    timestamp = datetime.fromtimestamp(int(submission["timestamp"])).strftime("%Y-%m-%d")

    print(f"Latest: {title} | Lang: {lang} | Date: {timestamp}")

    code = get_submission_code(sub_id, headers)
    problem_id, difficulty = get_difficulty(slug, headers)

    folder = DIFFICULTY_FOLDER.get(difficulty, "Easy")
    ext    = EXTENSIONS.get(lang, "txt")
    safe   = slug.replace("-", "_")
    fname  = f"{int(problem_id):04d}_{safe}.{ext}"

    header = (
        f"# {problem_id}. {title}\n"
        f"# Difficulty: {difficulty}\n"
        f"# Date: {timestamp}\n"
        f"# URL: https://leetcode.com/problems/{slug}/\n\n"
    )
    full_content = header + code
    commit_msg   = f"Add {difficulty} - {problem_id}. {title} ({timestamp})"

    push_to_github(folder, fname, full_content, commit_msg)
    print("Done!")

if __name__ == "__main__":
    main()

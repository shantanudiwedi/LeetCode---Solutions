
#!/usr/bin/env python3
"""
LeetCode → GitHub Auto-Sync
Fetches your latest accepted submission and pushes it to the correct folder.
"""
 
import os
import requests
import base64
import json
from datetime import datetime
 
# ── Config (set via environment variables or edit directly) ──────────────────
LEETCODE_SESSION = os.getenv("LEETCODE_SESSION", "")   # your LeetCode session cookie
GITHUB_TOKEN     = os.getenv("GITHUB_TOKEN", "")        # GitHub personal access token
GITHUB_REPO      = os.getenv("GITHUB_REPO", "username/leetcode-solutions")  # e.g. john/leetcode
# ────────────────────────────────────────────────────────────────────────────
 
EXTENSIONS = {
    "python3": "py", "python": "py",
    "java": "java", "cpp": "cpp", "c": "c",
    "javascript": "js", "typescript": "ts",
    "go": "go", "rust": "rs", "kotlin": "kt",
    "swift": "swift", "scala": "scala", "ruby": "rb",
}
 
DIFFICULTY_FOLDER = {
    "Easy":   "easy",
    "Medium": "medium",
    "Hard":   "hard",
}
 
 
def get_latest_submission():
    """Fetch the most recent accepted submission from LeetCode."""
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}",
        "Referer": "https://leetcode.com",
    }
    query = """
    query recentAcSubmissions {
      recentAcSubmissionList(username: "", limit: 1) {
        id
        title
        titleSlug
        timestamp
        lang
        code: __typename
      }
    }
    """
    # Use the submissions endpoint instead (more reliable)
    submissions_url = "https://leetcode.com/api/submissions/?offset=0&limit=1&lastkey="
    resp = requests.get(submissions_url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
 
    submissions = data.get("submissions_dump", [])
    if not submissions:
        raise ValueError("No submissions found. Check your LEETCODE_SESSION cookie.")
 
    latest = submissions[0]
    if latest["status_display"] != "Accepted":
        # Find the most recent accepted one
        submissions_url = "https://leetcode.com/api/submissions/?offset=0&limit=20&lastkey="
        resp = requests.get(submissions_url, headers=headers)
        data = resp.json()
        accepted = [s for s in data["submissions_dump"] if s["status_display"] == "Accepted"]
        if not accepted:
            raise ValueError("No accepted submissions found in recent history.")
        latest = accepted[0]
 
    return latest
 
 
def get_problem_difficulty(title_slug):
    """Fetch difficulty for a problem slug via LeetCode GraphQL."""
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}",
        "Referer": f"https://leetcode.com/problems/{title_slug}/",
    }
    query = {
        "query": """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            title
            difficulty
          }
        }
        """,
        "variables": {"titleSlug": title_slug},
    }
    resp = requests.post(url, json=query, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    question = data["data"]["question"]
    return question["questionId"], question["title"], question["difficulty"]
 
 
def push_to_github(folder, filename, content, commit_message):
    """Create or update a file in the GitHub repo."""
    api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{folder}/{filename}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }
 
    # Check if file already exists (to get its SHA for update)
    existing = requests.get(api_url, headers=headers)
    sha = existing.json().get("sha") if existing.status_code == 200 else None
 
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload = {
        "message": commit_message,
        "content": encoded,
    }
    if sha:
        payload["sha"] = sha
 
    resp = requests.put(api_url, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()["content"]["html_url"]
 
 
def slugify(title):
    """Convert problem title to a safe filename."""
    return title.lower().replace(" ", "_").replace("-", "_")
 
 
def main():
    if not LEETCODE_SESSION:
        print("❌  Set LEETCODE_SESSION environment variable.")
        print("    (See README for how to get it from your browser cookies.)")
        return
    if not GITHUB_TOKEN:
        print("❌  Set GITHUB_TOKEN environment variable.")
        return
 
    print("🔍  Fetching latest accepted submission...")
    submission = get_latest_submission()
 
    title_slug = submission["url"].strip("/").split("/")[-1]  # extract slug from URL
    lang = submission["lang"]
    code = submission["code"]
    ts = datetime.fromtimestamp(int(submission["timestamp"])).strftime("%Y-%m-%d")
 
    print(f"📄  Problem: {submission['title']}  |  Lang: {lang}")
 
    print("📊  Fetching difficulty...")
    problem_id, problem_title, difficulty = get_problem_difficulty(title_slug)
 
    folder = DIFFICULTY_FOLDER.get(difficulty, "easy")
    ext = EXTENSIONS.get(lang, "txt")
    safe_title = slugify(problem_title)
    filename = f"{problem_id:04d}_{safe_title}.{ext}"
 
    # Add a header comment to the file
    header = f"# {problem_id}. {problem_title}\n# Difficulty: {difficulty}\n# Date: {ts}\n# URL: https://leetcode.com/problems/{title_slug}/\n\n"
    full_content = header + code
 
    commit_msg = f"Add {difficulty} - {problem_id}. {problem_title} ({ts})"
 
    print(f"📁  Uploading to: {folder}/{filename}")
    url = push_to_github(folder, filename, full_content, commit_msg)
    print(f"✅  Uploaded! → {url}")
 
 
if __name__ == "__main__":
    main()
 

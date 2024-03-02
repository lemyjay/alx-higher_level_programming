#!/usr/bin/python3
'''
A Python script that takes 2 arguments in order to solve the challenge of
listing 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
Print all commits by: `<sha>: <author name>` (one by line)
'''
import requests
import sys


def get_commits(repo, owner):
    """Get the most recent 10 commits from a GitHub repository"""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {
        "per_page": 10,
        "page": 1,
        "order": "desc",
    }
    response = requests.get(url, params=params)
    commits = response.json()
    return commits


if __name__ == "__main__":
    repo, owner = sys.argv[1], sys.argv[2]
    commits = get_commits(repo, owner)

    for commit in commits:
        sha = commit["sha"]
        author = commit["commit"]["author"]["name"]
        print(f"{sha}: {author}")

#!/usr/bin/python3
"""Queries the Reddit API and prints the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "python:alu-scripting:v1.0 (by /u/ALUStudent)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        results = response.json().get("data", {}).get("children", [])

        if not results:
            print(None)
            return

        for post in results[:10]:
            print(post.get("data", {}).get("title"))

    except requests.RequestException:
        print(None)

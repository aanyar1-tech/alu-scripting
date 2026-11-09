#!/usr/bin/python3
"""
Module to query Reddit API and print top 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if not subreddit:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:alu.api.advanced:v1.0.0 (by /u/aanyar1)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        children = data.get("children", [])
        if not children:
            print(None)
            return
        for child in children:
            print(child.get("data", {}).get("title"))
    except Exception:
        print(None)

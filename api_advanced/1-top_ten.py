#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts.
"""

import requests
import sys


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'alu-api-advanced-student/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print(None)
            return

        for post in posts[:10]:
            title = post.get('data', {}).get('title')
            if title:
                print(title)

    except Exception:
        print(None)

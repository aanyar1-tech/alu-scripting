#!/usr/bin/python3
"""
Module to query the Reddit API and print the top 10 hot posts
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit. Prints None if invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'alu-scripting-user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json().get('data', {})
        posts = data.get('children', [])
        if not posts:
            print(None)
            return
        for post in posts:
            print(post.get('data', {}).get('title'))
    except ValueError:
        print(None)

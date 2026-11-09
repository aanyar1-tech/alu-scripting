#!/usr/bin/python3
"""
1-top_ten module
"""

import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'linux:alu.api.advanced:v1.0.0 (by /u/aanyar1)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])

        if not children:
            print(None)
            return None

        for child in children:
            print(child.get('data', {}).get('title'))
    except Exception:
        print(None)
        return None

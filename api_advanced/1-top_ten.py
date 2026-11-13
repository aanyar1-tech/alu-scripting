#!/usr/bin/python3
"""
Module to query Reddit API and print top 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'alu-scripting:top_ten:v1.0'}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        children = data.get('children', [])
        if not children:
            print(None)
            return

        for child in children[:10]:
            title = child.get('data', {}).get('title')
            if title:
                print(title)
    except Exception:
        print(None)

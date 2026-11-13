#!/usr/bin/python3
"""
1-top_ten module
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles
    of the first 10 hot posts for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python:alu-scripting:v1.2 (by /u/alu_student)'}

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

        data = response.json()
        children = data.get('data', {}).get('children', [])
        if not children:
            print(None)
            return

        for i in range(min(10, len(children))):
            title = children[i].get('data', {}).get('title')
            if title:
                print(title)
    except Exception:
        print(None)

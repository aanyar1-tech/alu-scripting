#!/usr/bin/python3
"""
Module to query the Reddit API and print the top 10 hot posts for a subreddit.
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
    headers = {'User-Agent': 'python3:alu-scripting:v1.0 (by /u/aanyar1-tech)'}

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
        
        # Check if the response contains valid data children
        if 'data' not in data or 'children' not in data.get('data', {}):
            print(None)
            return

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

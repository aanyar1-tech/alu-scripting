#!/usr/bin/python3
"""
Module to query the Reddit API and print the top 10 hot posts for a subreddit.
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python3:alu-scripting:v1.0 (by /u/aanyar1-tech)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        
        # If the subreddit is invalid, Reddit returns a redirect (302/301) or error status
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

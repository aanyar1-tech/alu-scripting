#!/usr/bin/python3
"""
Function to query the Reddit API and return the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the total number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'alu-scripting:v1.0 (by /u/aanyar1)'}
    
    # Disable automatic redirects to catch invalid subreddits/redirects
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        except ValueError:
            return 0
    return 0

#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:v1.0 (by /u/aanyar1)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        except ValueError:
            return 0
    return 0

#!/usr/bin/python3
"""
Module for recursive Reddit API hot posts listing.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursively returns a list containing the titles of all hot articles."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0.0"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
        after = data.get("after")
        count += data.get("dist", 0)
        for child in data.get("children", []):
            hot_list.append(child.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except Exception:
        return None

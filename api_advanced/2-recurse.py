#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Recursively queries Reddit API for hot articles of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/aanyar1)"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None if not hot_list else hot_list

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children and not hot_list:
            return None

        for child in children:
            hot_list.append(child.get("data", {}).get("title"))

        after = data.get("after")
        if after is not None:
            count += len(children)
            return recurse(subreddit, hot_list, after, count)

        return hot_list if hot_list else None
    except ValueError:
        return None if not hot_list else hot_list

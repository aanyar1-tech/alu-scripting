#!/usr/bin/python3
"""Queries Reddit API and prints top 10 hot posts"""
import requests

def top_ten(subreddit):
    """Prints titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for child in results.get("children"):
        print(child.get("data").get("title"))

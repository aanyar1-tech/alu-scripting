#!/usr/bin/python3
"""Queries Reddit API and counts keywords"""
import requests

:

def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in hot posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
        results = results.get("data")
        after = results.get("after")
        count += results.get("dist")
        for child in results.get("children"):
            title = child.get("data").get("title").lower().split()
            for word in word_list:
                if word.lower() in title:
                    times = len([t for t in title if t == word.lower()])
                    if instances.get(word.lower()) is None:
                        instances[word.lower()] = times
                    else:
                        instances[word.lower()] += times
    except Exception:
        pass
    if after is None:
        if len(instances) == 0:
            return
        instances = sorted(
            instances.items(), key=lambda kv: (-kv[1], kv[0])
        )
        for key, value in instances:
            print("{}: {}".format(key, value))
        return
    else:
        count_words(subreddit, word_list, instances, after, count)

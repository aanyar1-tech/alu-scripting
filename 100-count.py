#!/usr/bin/python3
"""
Module to parse and count keywords in hot posts.
"""

import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Recursively counts keyword occurrences in hot post titles."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0.0"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
        after = data.get("after")
        count += data.get("dist", 0)

        for child in data.get("children", []):
            title = child.get(
                "data", {}
            ).get("title", "").lower().split()
            for word in word_list:
                w_low = word.lower()
                times = title.count(w_low)
                if times > 0:
                    instances[w_low] = instances.get(w_low, 0) + times

        if after is not None:
            return count_words(
                subreddit, word_list, instances, after, count
            )

        if not instances:
            return

        sorted_instances = sorted(
            instances.items(), key=lambda kv: (-kv[1], kv[0])
        )
        for k, v in sorted_instances:
            print("{}: {}".format(k, v))
    except Exception:
        pass

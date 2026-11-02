#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, instances=None,
                word_counts=None, after=None):
    """Recursively queries Reddit API and counts occurrences of keywords."""
    if word_counts is None:
        word_counts = {}
        for word in word_list:
            w = word.lower()
            word_counts[w] = word_counts.get(w, 0) + 1

    if instances is None:
        instances = {w: 0 for w in word_counts}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/aanyar1)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children and after is None:
            return

        for child in children:
            title = child.get("data", {}).get("title", "").lower()
            words_in_title = title.split()
            cleaned_words = []
            for w in words_in_title:
                cleaned = w.strip(".,/#!$%^&*;:{}=\-_`~()[]?\"'")
                if cleaned:
                    cleaned_words.append(cleaned)

            for word in instances:
                instances[word] += cleaned_words.count(word)

        after = data.get("after")
        if after is not None:
            return count_words(
                subreddit, word_list, instances, word_counts, after
            )

        final_counts = {}
        for word, count in instances.items():
            total = count * word_counts[word]
            if total > 0:
                final_counts[word] = total

        if not final_counts:
            return

        sorted_words = sorted(
            final_counts.items(), key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_words:
            print("{}: {}".format(word, count))

    except Exception:
        return

#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces).
"""

import requests


def count_words(subreddit, word_list, after="", count=None):
    """
    Counts occurrences of keywords in the titles of hot posts on a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to search for.
        after (str, optional): The "after" parameter for pagination.
        count (list, optional): A list storing the counts of each keyword.

    Returns:
        None
    """
    if count is None:
        count = [0] * len(word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/126.0.0.0 Safari/537.36"
    }
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                for i, target_word in enumerate(word_list):
                    if target_word.lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            # Sorting by count and alphabetically
            sorted_counts = sorted(
                ((word_list[i].lower(), count[i]) for i in range(len(word_list)) if i not in save),
                key=lambda x: (-x[1], x[0])
            )

            for word, cnt in sorted_counts:
                if cnt > 0:
                    print(f"{word}: {cnt}")
        else:
            count_words(subreddit, word_list, after, count)

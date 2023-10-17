#!/usr/bin/python3
"""queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests


sesion = requests.Session()
sesion.headers.update({'User-agent': 'My User Agent'})
sesion.allow_redirects = False


def recurse(subreddit, hot_list=[]):
    URL = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    req = sesion.get(URL).json()
    try:
        for i in req['data']['children']:
            hot_list.append(i['data']['title'])
        if req['data']['after']:
            sesion.params = {'after': req['data']['after']}
            return recurse(subreddit, hot_list)
        return hot_list
    except Exception:
        return None

#!/usr/bin/env python3
"""Script for scraping some ESPN Tournament Challenge groups from:

- Top Groups: /topGroups
- Group Directory: /groupdir
- Suggested Groups: /groupfind

Base url: http://games.espn.go.com/tournament-challenge-bracket/2015/en/

Given group IDs, we can fetch brackets. Check `brackets.py`.

I already ran this and saved the output under `groups.txt`; so I do not
suggest you run this again unless necessary.
"""
import os
import re
import requests


host = 'http://games.espn.go.com/tournament-challenge-bracket/2015/en/'
r = re.compile('groupID=(\d+)')


def _fetch(path):
    resp = requests.get(host + path)
    return r.findall(resp.text)


def _groupdir():
    url = 'groupdir?&xhr=1&groupType=0&isLocked=0&access='
    groups = set()
    # Enumerate through private and public access groups.
    for i in range(1,3):
        u = url + str(i) + '&objectStart='
        # ESPN caps at 1000 groups.
        for t in range(0, 1000, 30):
            g = _fetch(u + str(t))
            groups.update(g)
    return groups


def _topgroups():
    url = 'topGroups?xhr=1&groupType='
    groups = set()
    for t in range(3):
        g = _fetch(url + str(t))
        groups.update(g)
    return groups


def _groupfind():
    g = _fetch('groupfind')
    return set(g)


def scrape_groups(filename='groups.txt'):
    g = _groupfind()
    g.update(_topgroups())
    g.update(_groupdir())
    g = sorted(map(int, g))
    with open(filename, 'w') as f:
        f.write(os.linesep.join(map(str, g)))
        print('Output written to {}'.format(filename))


if __name__ == '__main__':
    scrape_groups()

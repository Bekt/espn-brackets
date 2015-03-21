#!/usr/bin/env python3
"""Fetch all unique brackets in various ESPN Tournament groups.

I have already ran this script for groups in `groups.txt`, so please
try to avoid running with it again. Feel free to add new group IDs in 
`groups_manual.txt` and run this script.
"""
import os
import requests
import json
from multiprocessing.dummy import Pool


base = 'http://games-ak.espn.go.com/tournament-challenge-bracket/2015/en/api/v3/'


def by_group(group_id):
    url = base + 'group?length=10000&groupID=' + str(group_id)
    d = {}
    start = 0
    while True:
        try:
            resp = requests.get(url + '&start=' + str(start))
        except requests.exceptions.RequestException as e:
            print(group_id, e)
            continue
        data = json.loads(resp.text)
        if 'group' not in data or 'entries' not in data['group']:
            break
        else:
            ent = data['group']['entries']
            start += len(ent)
            for e in ent:
                eid = e['entryID']
                if eid not in d:
                    d[eid] = e['pickString']
    print(group_id)
    return d


def all_groups(files):
    groups = set()
    for f in files:
        with open(f, 'r') as fo:
            groups.update(fo.read().splitlines())
    pool = Pool(processes=os.cpu_count())
    results = pool.map(by_group, groups)
    pool.close()
    pool.join()
    entries = {}
    for r in results:
        entries.update(r)
    return entries


if __name__ == '__main__':
    fs = ['groups.txt', 'groups_manual.txt']
    out = 'brackets.txt'
    entries = all_groups(fs)
    with open(out, 'w') as f:
        tups = [str(k) + ' ' + v for k, v in entries.items()]
        f.write(os.linesep.join(tups))
        print('Output written to {}'.format(out))

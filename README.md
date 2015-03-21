## ESPN 2015 Brackets

This repository contains 3 million 2015 NCAA March Madness
brackets discovered on ESPN [group
directory](http://games.espn.go.com/tournament-challenge-bracket/2015/en/groupfind).

I have collected 2.9 million unique brackets that were found in 2047 ESPN
Tournament Challenge groups. These groups are provided in
`data/groups.txt` and can be viewed at:

`http://games.espn.go.com/tournament-challenge-bracket/2015/en/group?groupID=<group_id>`

## Bracket Format

First unzip `data/brackets.zip`. The format of each bracket is:

`<bracket_id> <picks>`, such as:

`4932920
01|03|05|07|09|11|13|15|17|19|21|23|25|28|30|31|33|35|37|39|42|43|45|47|49|51|53|55|58|60|61|63|01|07|09|15|17|23|25|30|33|39|43|47|49|53|58|63|01|15|17|30|39|47|49|63|15|17|39|49|15|49|49`

The full bracket can be viewed at:

`http://games.espn.go.com/tournament-challenge-bracket/2015/en/entry?entryID=<bracket_id>`

The `<picks>` string is in the form of:

`game1_winner_id|game2_winner_id|...|game63_winner_id`, where game numbers are:


* Midwest: `1-8, 33-36, 49-50, 57`
* West: `9-16, 37-40, 51-52, 58`
* East: `17-24, 41-44, 53-54, 59`
* South: `25-32, 45-48, 55-56, 60`
* Midwest vs. West: `61`
* East vs. South: `62`
* Final: `63`


And team IDs are:
```js
{'teams': [
   {'id': 1, 'name': 'Kentucky'},
   {'id': 2, 'name': 'Hampton'},
   {'id': 3, 'name': 'Cincinnati'},
   {'id': 4, 'name': 'Purdue'},
   {'id': 5, 'name': 'West Virginia'},
   {'id': 6, 'name': 'Buffalo'},
   {'id': 7, 'name': 'Maryland'},
   {'id': 8, 'name': 'Valparaiso'},
   {'id': 9, 'name': 'Butler'},
   {'id': 10, 'name': 'Texas'},
   {'id': 11, 'name': 'Notre Dame'},
   {'id': 12, 'name': 'Northeastern'},
   {'id': 13, 'name': 'Wichita St'},
   {'id': 14, 'name': 'Indiana'},
   {'id': 15, 'name': 'Kansas'},
   {'id': 16, 'name': 'NM State'},
   {'id': 17, 'name': 'Wisconsin'},
   {'id': 18, 'name': 'Coastal Car'},
   {'id': 19, 'name': 'Oregon'},
   {'id': 20, 'name': 'Oklahoma St'},
   {'id': 21, 'name': 'Arkansas'},
   {'id': 22, 'name': 'Wofford'},
   {'id': 23, 'name': 'UNC'},
   {'id': 24, 'name': 'Harvard'},
   {'id': 25, 'name': 'Xavier'},
   {'id': 26, 'name': 'Ole Miss'},
   {'id': 27, 'name': 'Baylor'},
   {'id': 28, 'name': 'Georgia St'},
   {'id': 29, 'name': 'VCU'},
   {'id': 30, 'name': 'Ohio State'},
   {'id': 31, 'name': 'Arizona'},
   {'id': 32, 'name': 'Texas So'},
   {'id': 33, 'name': 'Villanova'},
   {'id': 34, 'name': 'Lafayette'},
   {'id': 35, 'name': 'NC State'},
   {'id': 36, 'name': 'LSU'},
   {'id': 37, 'name': 'N Iowa'},
   {'id': 38, 'name': 'Wyoming'},
   {'id': 39, 'name': 'Louisville'},
   {'id': 40, 'name': 'UC Irvine'},
   {'id': 41, 'name': 'Providence'},
   {'id': 42, 'name': 'Dayton'},
   {'id': 43, 'name': 'Oklahoma'},
   {'id': 44, 'name': 'Albany'},
   {'id': 45, 'name': 'Michigan St'},
   {'id': 46, 'name': 'Georgia'},
   {'id': 47, 'name': 'Virginia'},
   {'id': 48, 'name': 'Belmont'},
   {'id': 49, 'name': 'Duke'},
   {'id': 50, 'name': 'R. Morris'},
   {'id': 51, 'name': 'San Diego St'},
   {'id': 52, 'name': "St. John's"},
   {'id': 53, 'name': 'Utah'},
   {'id': 54, 'name': 'SF Austin'},
   {'id': 55, 'name': 'Georgetown'},
   {'id': 56, 'name': 'E Washington'},
   {'id': 57, 'name': 'SMU'},
   {'id': 58, 'name': 'UCLA'},
   {'id': 59, 'name': 'Iowa State'},
   {'id': 60, 'name': 'UAB'},
   {'id': 61, 'name': 'Iowa'},
   {'id': 62, 'name': 'Davidson'},
   {'id': 63, 'name': 'Gonzaga'},
   {'id': 64, 'name': 'ND State'}
]}
```

## Extension

You are welcome to add more groups to `data/groups_manual.txt` (as long
as it doesn't exist in `data/groups.txt`) and run the script manually to
retrieve more brackets:

```bash
python3 brackets.py
```

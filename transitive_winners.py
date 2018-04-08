#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sets import Set

datafile = "score.csv"
list1 = ['Date','Win','Score1','Lose','Score2']
dict1 = {}
games = []

with open(datafile, "r") as f:
  for line in f:
    s = line.strip().split(",")
    for k,v in zip(list1,s):
      dict1[k] = v
    games += [dict1.copy()]
    dict1.clear()

teams = Set([i['Win'] for i in games] + [i['Lose'] for i in games])
WLTuple = [(i['Win'],i['Lose']) for i in games]

del list1, dict1, games

seed = ['Villanova']
tWinners = seed[:]

def get_transitive(seed,winners,WL):
  if seed == []:
    return winners
  seed = list(Set(map(lambda x: x[0], filter(lambda x: x[1] in seed, WL))))
  seed = filter(lambda x: x not in winners,seed)
  WL = filter(lambda x: x[1] not in winners, WL)
  winners = winners[:]
  winners += seed
#  print len(seed)
  return get_transitive(seed,winners,WL)

print "Total no. of teams: ", len(teams)
print "No. of transitive winning teams: ", len(get_transitive(seed,tWinners,WLTuple))

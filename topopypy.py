#topo.py

from cProfile import Profile
from pstats import Stats
from itertools import combinations, chain
import datetime

def powerset(n):
    s = range(n)
    return list(map(frozenset,chain.from_iterable(combinations(s, r) for r in range(n+1))))

def interunion(top):
    com = combinations(top, 2)
    for (x, y) in com:
        uni = frozenset(x.union(y))
        if uni not in top:
            return 0
        else:
            inter = frozenset(x.intersection(y))
            if inter not in top:
                return 0
    return 1


def checkdimen(n):
    print("start")
    po = powerset(n)
    print("make powerset")
    l = 2**n-2
    l2 = 2**l
    print("count topology")
    t=0
    r = 0
    poel = po[1:-1]
    y=0
    while y < l2:
        top = set()
        h=0
        while h < l:
            if (y//(2**h))%2 == 1:
                top.add(poel[h])
            h+=1
        top.update({po[0],po[-1]})
        t += interunion(top)
        if t % 10 == 0:
            f = t // 10
            if r != f:
                print(t)
                r = f
        y+=1
    print(t)
    return t
profile = Profile()
n = int(input('input cardinal number of topology: '))
profile.runcall(checkdimen,n)
stats = Stats(profile)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()

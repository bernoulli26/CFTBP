# topo.py

from itertools import combinations
import datetime


def powerset(n):
    l = []
    lis = range(n)
    m = "{0:0%db}" % n
    for i in range(2**n):
        j = m.format(i)
        jp = list(j)
        p = []
        for u in lis:
            if jp[u] == '1':
                p.append(lis[u])
        l.append(tuple(p))
    return l


def interunion(top):
    # basis=list()
    # for m in range(0,n):
    # arr = list(filter(lambda x: m in x,top))
    # arr.sort(key= lambda x: len(x))
    # basis+= [tuple(arr[0])]
    # basis=list(set(basis))
    # print(basis)
    com = combinations(top, 2)
    top = set(top)
    for (x, y) in com:
        uni = list(set(x).union(set(y)))
        uni.sort(key=lambda x: x)
        uni = tuple(uni)
        if uni not in top:
            return 0
        else:
            inter = list(set(x).intersection(set(y)))
            inter.sort(key=lambda x: x)
            inter = tuple(inter)
            if inter not in top:
                return 0
    return 1


def checktopo(top):
    # print(top)
    if not interunion(top):
        # print('not topology')
        return 0
    else:
        # print("topology set")
        return 1


def checkdimen(n):
    print("start")
    po = powerset(n)
    print("make powerset")
    l = 2**n-2
    l2 = 2**l
    po2 = po[1:-1]
    print("count topology")
    t = 0
    r = 0
    y = 0
    while y < l2:
        m = "{0:0%db}" % l
        jp = list(m.format(y))
        top = []
        for h in range(len(po2)):
            if jp[h] == "0":
                top.append(po2[h])
        top += [po[0], po[-1]]
        t += checktopo(top)
        if t % 10 == 0:
            f = t // 10
            if r != f:
                print(t)
                r = f
        y += 1
    return t

n = int(input('input cardinal number of topology: '))
start = datetime.datetime.now()
print(checkdimen(n))
end = datetime.datetime.now()-start
print(end)

#topo.py

from cProfile import Profile
from pstats import Stats
from itertools import combinations
import datetime
from multiprocessing import Process, Queue


def powerset(n):
    l = []
    i=0
    n2= 2**n
    while i < n2:
        p = []
        u=0
        while u < n:
            if (i//(2**u))%2 == 1:
                p.append(u)
            u+=1
        l.append(tuple(p))
        i+=1
    return l


def interunion(top):
    com = combinations(top, 2)
    for (x, y) in com:
        uni = list(set(x).union(set(y)))
        uni = tuple(sorted(uni))
        if uni not in top:
            return 0
        else:
            inter = list(set(x).intersection(set(y)))
            inter = tuple(sorted(inter))
            if inter not in top:
                return 0
    return 1


def proce(i,core,l,po,output):
    t=0
    r = 0
    l2 = 2**l
    poel = po[1:-1]
    while i < l2:
        top = []
        h = 0
        while h < l:
            if (i // (2 ** h)) % 2 == 1:
                top.append(poel[h])
            h += 1
        top += [po[0], po[-1]]
        t += interunion(top)
        if t % 10 == 0:
            f = t // 10
            if r != f:
                print(t)
                r = f
        i += core
    output.put(t)

def checkdimen(n):
    print("start")
    po = powerset(n)
    print("make powerset")
    l = 2**n-2
    print("count topology")
    core = 10
    t=0
    output = Queue()
    procs= [0]*core
    rancore = range(core)
    for i in rancore:
        procs[i] = Process(target=proce,args=(i,core,l,po,output))
    for i in rancore:
        procs[i].start()
        print('process %d start'%i)
    #process
    for i in rancore:
        procs[i].join()
        t += output.get()
        print('process %d end' % i)
    output.close()
    return t

if __name__=="__main__":
    profile = Profile()
    n = int(input('input cardinal number of topology: '))
    profile.run('checkdimen(n)')
    stats = Stats(profile)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()

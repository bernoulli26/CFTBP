# CFTBP
Count finite topology by python
===
It's a count finite topology which cardinal is n by python.
I made myself so it can be inefficient.
Now There are 3 files.
# 1 topo.py
it's the first program. 
That means most slow and uneffecient one.
```
On my labtop, n=4, it takes about 2 seconds with python 3.4.
if n>=5, it take too long so I gave up.
```
# 2 topopypy.py
it's a newer version.
it's made for operate on pypy.
So if you want to see how it be fast, you need to have pypy.
```
On my labtop, n=4, it takes about 0.2 seconds with pypy 2.7.
if n>=5, it take too long so I gave up.
```
# 3 topomulticore.py
it's made for operate with multiprocessing.
So you need multiprocessing module.
But I still don't know why it is slower than single core when using multi core.
If you know why, please leave me the answer.
```
On my labtop, n=4 with core = 1, it takes about 2 seconds with python 3.4.
On my labtop, n=4 with core = 2, it takes about 4 seconds with python 3.4.
On my labtop, n=4 with core = 3, it takes about 6 seconds with python 3.4.
On my labtop, n=4 with core = 10, it takes about 18 seconds with python 3.4.
if n>=5, it take too long so I gave up.
```
if you have a batter idea of code, please tell me so that improve this program.

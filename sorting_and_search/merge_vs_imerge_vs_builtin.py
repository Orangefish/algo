#fileencoding=utf-8
#!/usr/bin/env python3

from sort_merge import sorted_merge, sorted_merge_opt, sort_imerge
from random import shuffle
from timeit import timeit
import sys


# Resulst of sortin 1M Random list on Intel i3 2.4GHz, 8GB (2019):

"""
3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)]
win32
--------------
'B=sorted_merge(A)'            15.753644131000001
'B=sorted_merge_opt(A)'        15.587409749000003
'sort_imerge(A)'               51.91196010600001
'B=sorted(A)'                  0.7898158060000071

"""


if __name__ == '__main__':
    print(sys.version)
    print(sys.platform)
    print('--------------')
    Rand = list(range(1000000))
    shuffle(Rand)
    setup = 'A=list(Rand)'
    stmts = [   'B=sorted_merge(A)', 
                'B=sorted_merge_opt(A)', 
                'sort_imerge(A)', 
                'B=sorted(A)']
    for stmt in stmts:
        t = timeit(stmt=stmt, setup=setup, globals=globals(), number=1)
        print('{:<30} {:<10}'.format(repr(stmt),  t))


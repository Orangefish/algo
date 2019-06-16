#fileencoding=utf-8
#!/usr/bin/env python3

from sort_merge import sorted_merge
from bisection import sorted_binsert
from random import shuffle
from timeit import timeit
import sys


# Resulst of sortin 1M Random list on Intel i3 2.4GHz, 8GB (2019):
# The performance of sorted_binsert is very low baecause of insertion to list is
# has additional O(n) so overal time complexity of sorted_binsert is O(n^2 * log n)

"""
3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)]
win32
--------------
'B=sorted_merge(A)'            15.650651805999814
'B=sorted_binsert(A)'          152.03422072599983
'B=sorted(A)'                  0.7983889489999001

"""


if __name__ == '__main__':
    print(sys.version)
    print(sys.platform)
    print('--------------')
    Rand = list(range(1000000))
    shuffle(Rand)
    setup = 'A=list(Rand)'
    stmts = [   'B=sorted_merge(A)', 
                'B=sorted_binsert(A)', 
                'B=sorted(A)']
    for stmt in stmts:
        t = timeit(stmt=stmt, setup=setup, globals=globals(), number=1)
        print('{:<30} {:<10}'.format(repr(stmt),  t))


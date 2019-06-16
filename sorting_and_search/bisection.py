#fileencoding=utf-8
#!/usr/bin/env python3


"""
Search using bisection method.
Similar functionality in standrd module bisect, (see bisect_left, bisect_right)
"""

def bisect_idx_l(Seq, x):
    """Lefmost index for insertion x into sorted Seq.
    all Seq[:i] < x and Seq[i:] >= x

    Time: O(log n)
        
    Space (additional): O(1) 

    >>> A = [2, 3]
    >>> bisect_idx_l(A, 4) == 2
    True
    >>> bisect_idx_l(A, 1) == 0
    True
    >>> A = [3, 3]
    >>> bisect_idx_l(A, 3) == 0
    True
    """

    l = 0
    r = len(Seq)
    while l < r:
        m = l + (r - l)//2
        if x<= Seq[m]:
            r = m
        else:
            l = m + 1
    return l


def bisect_idx_r(Seq, x):
    """Rightmost index for insertion x into sorted Seq.
    all Seq[:i] <= x and Seq[i:] > x

    Time: O(log n)
        
    Space (additional): O(1) 

    >>> A = [2, 3]
    >>> bisect_idx_r(A, 4) == 2
    True
    >>> bisect_idx_r(A, 1) == 0
    True
    >>> A = [3, 3]
    >>> bisect_idx_r(A, 3) == 2
    True
    """
    l = 0
    r = len(Seq)
    while l < r:
        m = l + (r - l)//2
        if x < Seq[m]:
            r = m
        else:
            l = m + 1
    return r

def search_l(Seq, x):
    """Lefmost index for insertion x into sorted Seq.

    Time: O(log n)
        
    Space (additional): O(1) 

    >>> A = [3, 3]
    >>> search_l(A, 3) == 0
    True

    """
    i = bisect_idx_l(Seq, x) 
    return i if i<len(Seq) and Seq[i] == x else -1

def search_r(Seq, x):
    """Rightmost index for insertion x into sorted Seq.

    Time: O(log n)
        
    Space (additional): O(1) 

    >>> A = [3, 3]
    >>> search_r(A, 3) == 1
    True

    """
    i = bisect_idx_r(Seq, x) 
    return i-1 if i-1<len(Seq) and Seq[i-1] == x else -1

from functools import reduce
def sorted_binsert(Seq):
    """Sorting using insertion into sorted Seq.
    The index is  determined by bisection method.

    The performance is very low O(n^2 * log n) 
    Because list is used as resulting structure,
    each insertion in list has O(n) time complexity.

    Time: O(n * n * log n) = O(n^2 * log n)
        n -- elements in initial Seq
        n -- average comlexity of insertion operation
        log n -- search for position
            
    Space (additional): O(n) 
        creates new sequence with same len as input sequence 

    >>> A = [2, 1]
    >>> A = sorted_binsert(A)
    >>> A == [1, 2] 
    True

    >>> A = [1, 2]
    >>> A = sorted_binsert(A)
    >>> A == [1, 2] 
    True
    
    >>> import random
    >>> A = list(range(100))
    >>> random.shuffle(A)
    >>> A = sorted_binsert(A)
    >>> A == list(range(100))
    True

    """

    def _insert_l_(L, e):
        i = bisect_idx_l(L, e)
        L.insert(i, e)
        return L
    return reduce(_insert_l_, Seq, []) 
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

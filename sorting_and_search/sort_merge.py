#fileencoding=utf-8
#!/usr/bin/env python3


def sorted_merge(Seq):
    """ Merge sorting, unmutable input. 
    Output is recreated input.
    
    Time: O(n * log n)
        log n -- levels
        n -- elements on each level must be merged
            
    Space (additional): O(n) 
        creates new sequence with same len as input sequence 

    Returns list

    >>> A = [3, 2, 1]
    >>> B = sorted_merge(A)
    >>> B == [1, 2, 3] 
    True

    >>> A = [1, 2, 3]
    >>> B = sorted_merge(A)
    >>> B == [1, 2, 3] 
    True

    >>> A = [1]
    >>> B = sorted_merge(A)
    >>> A is B
    False
    
    >>> import random
    >>> A = list(range(100))
    >>> random.shuffle(A)
    >>> B = sorted_merge(A)
    >>> B == list(range(100))
    True

    """
    if len(Seq) > 1:
        m = len(Seq)//2
        A = sorted_merge(Seq[0:m])
        B = sorted_merge(Seq[m:])
        C = []
        i=j=0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        while i < len(A):
                C.append(A[i])
                i += 1
        while j < len(B):
                C.append(B[j])
                j += 1
        return C
    else:
        return list(Seq)

def sorted_merge_opt(Seq, l=0, u=None):
    """ Merge sorting, unmutable input. 
    Output is recreated input.
    Optimizations - indexes is used as much as possible for Seq 
    splitting instead of slicing and recreating.
    
    Time: O(n * log n)
        log n -- levels
        n -- elements on each level must be merged
            
    Space (additional): O(n) 
        creates new sequence with same len as input sequence 

    Returns list

    >>> A = [3, 2, 1]
    >>> B = sorted_merge_opt(A)
    >>> B == [1, 2, 3] 
    True

    >>> A = [1, 2, 3]
    >>> B = sorted_merge_opt(A)
    >>> B == [1, 2, 3] 
    True

    >>> A = [1]
    >>> B = sorted_merge_opt(A)
    >>> A is B
    False
    
    >>> import random
    >>> A = list(range(100))
    >>> random.shuffle(A)
    >>> B = sorted_merge_opt(A)
    >>> B == list(range(100))
    True

    """
    u = len(Seq) if u is None else u
    if u - l > 1:
        m = l + (u - l)//2
        A = sorted_merge_opt(Seq, l, m)
        B = sorted_merge_opt(Seq, m, u)
        C = [0] * (u - l) 
        i=j=k=0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C[k] = A[i]
                i += 1
            else:
                C[k] = B[j]
                j += 1
            k += 1
        while i < len(A):
                C[k] = A[i]
                i += 1
                k += 1
        while j < len(B):
                C[k] = B[j]
                j += 1
                k += 1
        return C
    else:
        return Seq[l:u]

def sort_imerge(Seq, l=0, u=None):
    """ Merge sorting, mutable input. 
    Input sequence changed in place. 
    Uses 2 auxilary functions wsort and wmerge.
    Inplace method works slower than methods with additional memory allocation.

    Time: O(n * log n)
        log n -- levels
        n -- elements on each level must be merged
            
    Space (additional): O(1) 
        input changed in place

    Returns None

    Based on:
    https://github.com/liuxinyu95/AlgoXY/blob/algoxy/sorting/merge-sort/src/mergesort.c
    https://stackoverflow.com/questions/2571049/how-to-sort-in-place-using-the-merge-sort-algorithm/15657134#15657134

    >>> A = [3, 2, 1]
    >>> sort_imerge(A)
    >>> A == [1, 2, 3] 
    True
    
    >>> A = [1, 2, 3]
    >>> sort_imerge(A)
    >>> A == [1, 2, 3] 
    True

    >>> import random
    >>> A = list(range(100))
    >>> random.shuffle(A)
    >>> sort_imerge(A)
    >>> A == list(range(100))
    True

    """
    u = len(Seq) if u is None else u
    if  u - l > 1:
        m = l + (u - l) // 2
        w = l + u - m  
        wsort(Seq, l, m, w)
        while w - l > 2:
            n = w
            w = l + (n - l + 1) // 2
            wsort(Seq, w, n, l)
            wmerge(Seq, l, l + n - w, n, u, w)
        n = w
        while n > l: # fallback to insert sort
            for m in range(n, u):
                if Seq[m-1] > Seq[m]:
                    Seq[m-1], Seq[m] = Seq[m], Seq[m-1]
            n -= 1

def wmerge(Seq, i, m, j, n, w):
    """Merge subarrays [i, m) and [j, n) into work area w.
    All indexes point into Seq.
    The space after w must be enough to fit both subarrays.

    1st      i  m
    2nd         j  n
    wka            w
    >>> L = [5, 4, 0, 0]
    >>> wmerge(L, 0, 1, 1, 2, 2) 
    >>> L == [0, 0, 4, 5]
    True

    1st      i        m
    2nd               j        n
    wka                        W                
    >>> L = [4, 5, 6, 1, 2, 3, 0, 0, 0, 0, 0, 0]
    >>> wmerge(L, 0, 3, 3, 6, 6) 
    >>> L == [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6]
    True

    """
    while i < m and j < n:
        if Seq[i] < Seq[j]:
            Seq[i], Seq[w] = Seq[w], Seq[i]
            i += 1
        else:
            Seq[j], Seq[w] = Seq[w], Seq[j]
            j += 1
        w += 1
    while i < m:
        Seq[i], Seq[w] = Seq[w], Seq[i]
        i += 1
        w += 1
    while j < n:
        Seq[j], Seq[w] = Seq[w], Seq[j]
        j += 1
        w += 1

def wsort(Seq, l, u, w):
    """Sort subarray [l, u) and put reuslt into work area w.
    All indexes point into Seq.

    arr      l  u
    wka         w
    >>> L = [9, 0]
    >>> wsort(L, 0, 1, 1) 
    >>> L == [0, 9]
    True

    arr      l     u
    wka            w
    >>> L = [5, 4, 0, 0]
    >>> wsort(L, 0, 2, 2) 
    >>> L == [0, 0, 4, 5]
    True

    arr      l                 u
    wka                        w
    >>> L = [5, 6, 1, 4, 2, 3, 0, 0, 0, 0, 0, 0]
    >>> wsort(L, 0, 6, 6) 
    >>> L == [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6]
    True


    """
    if  u - l > 1:
        m = l + (u - l) // 2
        sort_imerge(Seq, l, m)
        sort_imerge(Seq, m, u)
        wmerge(Seq, l, m, m, u, w)
    else:
        while l < u:
            Seq[l], Seq[w] = Seq[w], Seq[l]
            l +=1
            w +=1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

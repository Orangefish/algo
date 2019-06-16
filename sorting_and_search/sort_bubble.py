#fileencoding=utf-8
#!/usr/bin/env python3


def sort_bub(Seq):
    """Buble sorting.
    Input sequence changed in place. 

    Time: O(n * n)
    Space (additional): O(1)

    Returns None 

    >>> A = [3, 2, 1]
    >>> sort_bub(A)
    >>> A == [1, 2, 3] 
    True

    >>> A = [1, 2, 3]
    >>> sort_bub(A)
    >>> A == [1, 2, 3] 
    True
    
    >>> import random
    >>> A = list(range(100))
    >>> random.shuffle(A)
    >>> sort_bub(A)
    >>> A == list(range(100))
    True

    """
    if len(Seq) > 1:
        exchange = True
        while exchange:
            exchange = False 
            for i in range(len(Seq)-1):
                if Seq[i] > Seq[i+1]:
                    Seq[i], Seq[i+1] = Seq[i+1], Seq[i]
                    exchange = True

if __name__ == '__main__':
    import doctest
    doctest.testmod()

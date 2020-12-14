from collections import deque
def tail(n, iterable):
    "Return an iterator over the last n items"
    # tail(3, 'ABCDEFG') --> E F G
    return iter(deque(iterable, maxlen=n))

from functools import reduce
from functools import lru_cache
from operator import mul

def _extended_euclidean_algorithm ( a , b , sa = 1 , ta = 0 , sb = 0 , tb = 1 ) :

    assert(sa * sb <= 0)
    assert(ta * tb <= 0)

    yield (a, sa, ta)
    if b == 0:
        yield (b, sb, tb)

    else:
        q, _a = a // b, a % b
        _sa = sa - q * sb
        _ta = ta - q * tb
        yield from _extended_euclidean_algorithm( b, _a, sb, tb, _sa, _ta)

def extended_euclidean_algorithm ( a , b ) :
    for step, (d,x,y) in enumerate(_extended_euclidean_algorithm(a,b)):
        assert(b == 0 or abs(x) <= b)
        assert(a == 0 or abs(y) <= a)
        assert(d == x * a + y * b)
        if step % 2 == 0:
            assert(x > 0)
            assert(y <= 0)
        else:
            assert(x <= 0)
            assert(y > 0)
        yield d, x, y

def egcd ( a , b ):
    assert(a >= b)
    it = tail(2, extended_euclidean_algorithm(a, b))
    r, sa, ta = next(it)
    _, sb, tb = next(it)
    assert(_ == 0)
    return (r, sa, ta, sb, tb)

if __name__ == '__main__':

    import sys

    gcd = {}
    c = {}

    k = int(sys.argv[1])
    for i in range(k,1,-1):
        mi = 2**i - 1
        for j in range(i+1, k+1):
            mj = 2**j - 1
            r, sa, ta, sb, tb = egcd(mj, mi)
            gcd[(i,j)] = r
            c[(i,j)] = ta % mj

    print(gcd)
    print(c)


    product = lambda iterable: reduce(mul, iterable, 1)
    score = lambda m: product(map(lambda i: 2**i - 1, m))

    # greedy
    def greedy(n):
        m = set()
        for i in range(n,1,-1):
            if all(map(lambda j: gcd[(i,j)] == 1, m)):
                m.add(i)

        return m

    @lru_cache(maxsize=None)
    def dp(candidates):
        if not candidates: return frozenset()
        j = max(candidates)
        others = candidates - {j}
        compatible = frozenset(filter(lambda i: gcd[(i,j)] == 1, others))
        return max(frozenset([j]) | dp(compatible), dp(others), key=score)

    for n in range(2,k+1):
        g = greedy(n)
        print(g, sum(g), score(g))

    for n in range(2,k+1):
        g = dp(frozenset(range(2, n+1)))
        print(g, sum(g), score(g))

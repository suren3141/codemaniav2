import sys
from moraxtreme_5.Perm.solve import *

def test_input(f_in):
    t = read_ints(f_in)[0]
    assert 1 <= t <= 10

    for __ in range(t):
        l, n = read_ints(f_in)

        assert 1 <= l <= 10**9
        assert 1 <= n <= 10**5

        arr =read_ints(f_in)

        assert len(arr) == n

        for i in arr:
            assert 1 <= i <= 10**5


def comp(f_in, f_out):
    pass

if __name__ == "__main__":


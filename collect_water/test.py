import sys
from moraxtreme_5.Perm.solve import *

def test_input(f_in):
    t = int(f_in.readline())
    assert 1 <= t <= 10

    for x in range(t):

        n = int(f_in.readline())
        arr = read_ints(f_in)

        assert len(arr) == n
        assert 1 <= n <= 10**6

        for i in arr:
            assert 0 <= i <= 10**9


def comp(f_in, f_out):
    pass


if __name__ == "__main__":

    for i in range(1, 2):
        f_in = open("ex%d.txt"%i, 'r')
        comp(f_in, sys.stdout)


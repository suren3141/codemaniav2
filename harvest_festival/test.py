import sys
from moraxtreme_5.Perm.solve import *

def test_input(f_in):
    t = read_ints(f_in)[0]
    assert 1 <= t <= 10

    for __ in range(t):
        n, k = read_ints(f_in)

        assert 1 <= k <= n <= 10**5

        speed = read_ints(f_in)
        efficiency = read_ints(f_in)

        assert len(speed) == n
        assert len(efficiency) == n

        for (i, j) in zip(speed, efficiency):
            assert 1 <= i <= 10**9
            assert 1 <= j <= 10**9


def comp(f_in, f_out):
    pass

if __name__ == "__main__":

    for i in range(1, 2):
        f_in = open("ex%d.txt"%i, 'r')
        comp(f_in, sys.stdout)


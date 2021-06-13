import sys
import string
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]


def test_input(f_in):
    t = read_ints(f_in)[0]
    assert 1 <= t <= 100

    for __ in range(t):
        n, s = f_in.readline().strip().split()
        n = int(n)

        assert len(s) == n
        assert 1 <= n <= 10**4

        for i in s:
            assert i in string.ascii_lowercase


def comp(f_in, f_out):
    raise NotImplementedError

if __name__ == "__main__":

    for i in range(1, 2):
        f_in = open("ex%d.txt"%i, 'r')
        comp(f_in, sys.stdout)


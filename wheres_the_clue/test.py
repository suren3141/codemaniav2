import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def test_input(f_in):
    t =read_ints(f_in)[0]
    assert 1 <= t <= 10**5

    for __ in range(t):
        n, x, y = read_ints(f_in)
        assert 1 <= n <= 10**9
        assert 1 <= x <= 10**4
        assert 1 <= y <= 10**4



def comp(f_in, f_out):
    raise NotImplementedError

if __name__ == "__main__":

    for i in range(1, 2):
        f_in = open("ex%d.txt"%i, 'r')
        comp(f_in, sys.stdout)


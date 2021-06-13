import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]


def test_input(f_in):
    n = read_ints(f_in)[0]

    assert 1 <= n <= 10**9+7


def comp(f_in, f_out):
    raise NotImplementedError

if __name__ == "__main__":

    for i in range(1, 2):
        f_in = open("ex%d.txt"%i, 'r')
        comp(f_in, sys.stdout)


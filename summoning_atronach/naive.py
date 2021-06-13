import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def naive():

    ans = -1
    return ans


def solve_naive(f_in, f_out):
    t = read_ints(f_in)[0]

    for __ in range(t):
        n, x, y = read_ints(f_in)

        ans = naive()

        f_out.write("%d\n" % ans)


if __name__ == "__main__":
    solve_naive(sys.stdin, sys.stdout)

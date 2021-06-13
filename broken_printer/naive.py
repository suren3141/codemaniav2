import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def naive():

    ans = -1
    return ans


def solve_naive(f_in, f_out):
    n = read_ints(f_in)[0]

    i = 0
    while n > 0:
        i += 1
        n -= len(str(i))

    ans = i if n == 0 else -1

    f_out.write("%d\n" % ans)


if __name__ == "__main__":
    solve_naive(sys.stdin, sys.stdout)

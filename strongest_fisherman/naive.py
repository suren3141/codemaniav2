import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def naive():

    ans = -1
    return ans


def solve_naive(f_in, f_out):
    n, m = read_ints(f_in)

    arr = []

    for __ in range(n):
        x, y = read_ints(f_in)
        arr.append(max(abs(x), abs(y)))

    arr = sorted(arr)

    for __ in range(m):
        d = read_ints(f_in)[0]

        ans = 0
        while arr[ans] <= d and ans < n:
            ans += 1

        f_out.write("%d\n" % ans)


if __name__ == "__main__":
    solve_naive(sys.stdin, sys.stdout)

import sys
import bisect


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]


MOD = 10**15 + 9



def solve(f_in, f_out):

    n, m = read_ints(f_in)
    assert 1 <= n <= 1e5
    assert 1 <= m <= 1e5

    arr = []

    for __ in range(n):
        x, y = read_ints(f_in)
        assert -1e9 <= x <= 1e9
        assert -1e9 <= y <= 1e9
        arr.append(max(abs(x), abs(y)))

    arr = sorted(arr)

    for __ in range(m):
        d = read_ints(f_in)[0]
        assert 0 <= d <= 1e9

        num = bisect.bisect_right(arr, d)
        f_out.write("%d\n"%num)



if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

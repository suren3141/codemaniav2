import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]


MOD = 10**9 + 7
def naive(n, x, y):

    count = 0
    ans = 0
    while count < n:
        ans += 1
        if ans %x == 0 or ans % y == 0:
            count += 1

    return ans % MOD



def solve_naive(f_in, f_out):

    t =read_ints(f_in)[0]
    assert 1 <= t <= 10**5

    for __ in range(t):
        n, x, y = read_ints(f_in)

        ans = naive(n, x, y)



        f_out.write("%d\n"%ans)


if __name__ == "__main__":

    solve_naive(sys.stdin, sys.stdout)

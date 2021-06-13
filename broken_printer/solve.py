import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def solve_util(n, arr):
    raise NotImplementedError




def solve(f_in, f_out):

    count = [9 * 10**i for i in range(10)]
    eprint(count)

    VALID = False

    n = int(f_in.readline())
    base = 0
    ans = 0
    val = 0
    base = 1

    for i,x in enumerate(count):
        val = x * (i+1)
        if n >= val:
            n -= val
            ans += x
            base += 1
        else:
            break

    if n % base == 0:
        ans += n // base
    else:
        ans = -1

    f_out.write("%d\n"%ans)

    return -1 <= ans <= 10**9 + 7


if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

import sys
from solve import *

def naive(xxx):

    ans = -1
    return ans


def solve_naive(f_in, f_out):

    n = int(f_in.readline())
    xxx = read_ints(f_in)

    ans = naive(xxx)

    f_out.write("%d\n"%ans)


if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

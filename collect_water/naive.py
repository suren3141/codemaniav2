import sys
def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def naive(xxx):

    ans = -1
    return ans


def solve_naive(f_in, f_out):

    n = int(f_in.readline())
    arr = read_ints(f_in)

    tot = 0

    f_out.write("%d\n"%ans)


if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def solve_util(n, arr):
    raise NotImplementedError




def solve(f_in, f_out):

    x, y, z = read_ints(f_in)
    x, y, z = sorted([x, y, z])

    if y-x == z-y:
        ans = x-(y-x)
        if ans <= 0: ans = z + (y-x)

    elif 2*(y - x) == z - y:
        d = y-x
        ans = y + d

    elif (y - x) == 2 *(z - y):
        d = z - y
        ans = y - d

    else:
        ans = -1

    f_out.write("%d\n"%ans)

    return True


if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

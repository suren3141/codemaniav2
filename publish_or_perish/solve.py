import sys
from collections import defaultdict

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def solve_util(xxx):

    ans = -1
    return ans




def solve(f_in, f_out):

    dic = defaultdict(list)

    n, q = read_ints(f_in)
    arr = read_ints(f_in)
    for i in range(n):
        pub = f_in.readline().strip().split()
        cite = int(pub[0])
        for auth in pub[1:]:
            dic[auth].append(cite)

    for i in range(q):
        auth = f_in.readline().strip()
        ans = 0
        if auth in dic:
            pub = sorted(dic[auth])
            for j in range(len(pub)):
                if pub[-j-1] > ans:
                    ans += 1
                else:
                    break

        f_out.write("%d\n"%ans)


if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

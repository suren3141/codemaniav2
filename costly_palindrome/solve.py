import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def solve_util(n, arr):
    raise NotImplementedError




def solve(f_in, f_out):

    VALID = False

    t = read_ints(f_in)[0]

    for __ in range(t):
        n, s = f_in.readline().strip().split()
        n = int(n)

        count = [0 for i in range(26)]
        for c in s:
            count[ord(c)-ord('a')] += 1

        eprint(count)
        ans = sum([i%2 for i in count])
        if ans > 0: ans -=1

        VALID = VALID or 0 < ans < n-1

        f_out.write("%d\n"%ans)

    return VALID


if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

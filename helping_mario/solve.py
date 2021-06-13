import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]


MOD = 10 ** 9 + 7



def solve(f_in, f_out):

    t = read_ints(f_in)[0]

    for __ in range(t):

        tot, k = read_ints(f_in)

        sticks = read_ints(f_in)

        sticks.sort()

        number = 0

        for i in range(0, k):
            if tot >= sticks[i]:
                tot = tot - sticks[i]
                number = number + 1
            else:
                break

        ans = "%d"%(number)

        f_out.write("%s\n"%ans)

if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

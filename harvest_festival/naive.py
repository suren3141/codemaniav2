import sys, os
import bisect
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]


MOD = 10**9 + 7
def naive(n, k, speed, efficiency):
    arr = [(efficiency[i], speed[i]) for i in range(n)]
    arr = sorted(arr)

    efficiency = [arr[i][0] for i in range(n)]
    speed = [arr[i][1] for i in range(n)]

    ans = 0
    tot = 0
    for i in range(-1, -k-1, -1):
        e = efficiency[i]
        tot += speed[i]

        ans = max(ans, e * tot)

    h = sorted(speed[-k:])

    for i in range(-k-1, -n-1, -1):
        e = efficiency[i]
        bisect.insort(h, speed[i])

        tot = sum(h[-k:])

        ans = max(ans, tot*e)

    return ans%MOD


def naive2(n, k, speed, efficiency):
    arr = [(efficiency[i], speed[i]) for i in range(n)]
    arr = sorted(arr)

    efficiency = [arr[i][0] for i in range(n)]
    speed = [arr[i][1] for i in range(n)]

    ans = 0
    tot = 0
    for i in range(-1, -k - 1, -1):
        e = efficiency[i]
        tot += speed[i]

        ans = max(ans, e * tot)
        # eprint(i, e, tot, ans)

    h = speed[-k:]

    for i in range(-k - 1, -n - 1, -1):
        e = efficiency[i]
        s = speed[i]

        min_ind = -1
        min_val = s
        for j in range(k):
            if h[j] < min_val:
                min_val = h[j]
                min_ind = j

        if min_ind != -1:
            h[min_ind] = s
            tot += s - min_val

        ans = max(ans, tot * e)
        # eprint(i, e, tot, ans)

    return ans % MOD


def solve_naive(f_in, f_out):

    t = read_ints(f_in)[0]

    for __ in range(t):

        n, k = read_ints(f_in)
        eprint(n, k)

        speed = read_ints(f_in)
        efficiency = read_ints(f_in)

        ans = naive2(n, k, speed, efficiency)

        f_out.write("%d\n"%ans)


if __name__ == "__main__":

    solve_naive(open("./input/input10.txt", 'r'), open("./temp.txt", 'w+'))

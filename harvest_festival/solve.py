import sys
import heapq


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]


def solve_util(xxx):
    ans = -1
    return ans


MOD = 10 ** 9 + 7


def solve(f_in, f_out):
    VALID = True

    t = read_ints(f_in)[0]

    for __ in range(t):

        n, k = read_ints(f_in)

        speed = read_ints(f_in)
        efficiency = read_ints(f_in)

        arr = [(efficiency[i], speed[i]) for i in range(n)]
        arr = sorted(arr)

        efficiency = [arr[i][0] for i in range(n)]
        speed = [arr[i][1] for i in range(n)]

        # print(speed, efficiency)

        ans = 0
        tot_speed = 0

        for i in range(-1, -k - 1, -1):
            e = efficiency[i]

            tot_speed += speed[i]
            # print(tot_speed, e)

            ans = max(ans, tot_speed * e)

        h = speed[-k:]
        heapq.heapify(h)

        for i in range(-k - 1, -n - 1, -1):
            e = efficiency[i]

            val = heapq.heappushpop(h, speed[i])

            # print(g)

            # print(i, e, val)
            # g.print_util(g.root, 0)

            tot_speed = tot_speed + speed[i] - val
            # print(tot_speed, e)

            ans = max(ans, tot_speed * e)

        ans = ans % MOD

        VALID = VALID and ans < MOD * 10000

        f_out.write("%d\n" % ans)

    return VALID


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)

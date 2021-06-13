import sys
import math
MOD = 10**9 + 7

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]

def solve_util(n, x, y):
    ans = 0
    lcm = (x*y)//math.gcd(x, y)

    lcm_count = (lcm // x) + (lcm // y) - 1

    start = n // lcm_count
    # eprint('--------', n-start*lcm_count, n, lcm_count, start)
    n -= start * lcm_count

    if n > 0:

        left = min(x, y)    # n=1
        right = lcm         # n=lcm_count
        mid = (right + left) // 2
        # eprint('---------', mid, left, right)

        while right > left:
            val = mid//x + mid//y

            if val < n:
                left = mid+1
            else:
                right = mid

            mid = (right + left) // 2

            # eprint(val, mid, left, right)


        ans = mid

    ans += (start % MOD *lcm % MOD) % MOD

    return ans % MOD





def solve(f_in, f_out):

    VALID = True

    t = read_ints(f_in)[0]

    for __ in range(t):
        n, x, y = read_ints(f_in)
        ans = solve_util(n, x, y)

        VALID = VALID and 0 <= ans < MOD

        f_out.write("%d\n"%ans)

    return VALID


if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

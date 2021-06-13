import sys

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

    t = int(f_in.readline())

    for __ in range(t):

        n = int(f_in.readline())
        arr = read_ints(f_in)

        ans = sum(arr)

        arr = sorted(list(enumerate(arr)),key=lambda x:x[1], reverse=True)

        # eprint(arr)

        mx_idx, mx_val = arr[0]
        left = mx_idx
        right = mx_idx

        tot = 0

        for (idx, val) in arr[1:]:
            if idx < left:
                tot += (mx_val-val)*(left-idx)
                left = idx
            elif idx > right:
                tot += (mx_val-val)*(idx-right)
                right = idx

        ans = mx_val * n - ans - tot

        VALID = VALID and 0 <= VALID <= MOD*10000

        ans = ans % MOD


        f_out.write("%d\n"%ans)

    return VALID


if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

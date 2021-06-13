import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def read_ints(f_in=sys.stdin):
    return [int(i) for i in f_in.readline().strip().split()]


MOD = 10 ** 9 + 7


class BST:

    def __init__(self, vals=None):

        if vals is None: vals = []
        self.root = None

        for v in vals:
            self.bst_insert(v)

    def bst_insert(self, node):
        if self.root == None:
            self.root = node
        else:
            self.insert_util(self.root, node)

    def insert_util(self, root, node):
        if root.val < node.val:
            if root.right == None:
                root.right = node
            else:
                self.insert_util(root.right, node)
        else:
            if root.left == None:
                root.left = node
            else:
                self.insert_util(root.left, node)

    def __repr__(self):
        l = 0
        done = False
        arr = [[self.root]]

        while not done:
            done = True
            arr.append([])
            print(arr)
            for i in range(2 << l):
                node = arr[l][i]
                if node is not None:
                    done = False
                    arr[-1] += [node.left, node.right]

                l += 1

        for i in range(l):
            sep = "\t" * ((2 << (l - i - 1)) - 1)
            arr[i] = sep + 2 * sep.join([str(node.val) if node is not None else '-' for node in arr[i]])

        return "\n".join(arr)

    def print_util(self, root, i):
        if root == None:
            return
        self.print_util(root.left, i + 1)
        print(root.val, i)
        self.print_util(root.right, i + 1)

    def pop_min(self):

        if self.root.left is None:
            min_val = self.root.val
            self.root = self.root.right

        else:
            gpar = self.root
            par = gpar.left

            while par.left is not None:
                gpar = par
                par = par.left

            min_val = par.val
            gpar.left = par.right

        return min_val


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


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

        g = BST()
        ans = 0
        tot_speed = 0

        for i in range(-1, -k - 1, -1):
            e = efficiency[i]
            g.bst_insert(Node(speed[i]))

            # print(g)

            tot_speed += speed[i]
            # print(tot_speed, e)

            ans = max(ans, tot_speed * e)

        for i in range(-k - 1, -n - 1, -1):
            e = efficiency[i]
            g.bst_insert(Node(speed[i]))
            val = g.pop_min()

            # print(g)

            # print(i, e, val)
            # g.print_util(g.root, 0)

            tot_speed = tot_speed + speed[i] - val
            # print(tot_speed, e)

            ans = max(ans, tot_speed * e)

        ans = ans % MOD

        VALID = VALID and ans < MOD*10000

        f_out.write("%d\n"%ans)

    return VALID

if __name__ == "__main__":

    solve(sys.stdin, sys.stdout)

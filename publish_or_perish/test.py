import sys
from moraxtreme_5.Perm.solve import *

def comp(f_in, f_out):
    raise NotImplementedError


def test_input(f_in):

    n, q = read_ints(f_in)
    assert 1 <= n <= 1000
    assert 1 <= q <= 1000

    arr = read_ints(f_in)
    assert len(arr) == n
    for k in arr:
        assert 1 <= k <= 1000

    for i in range(n):
        pub = f_in.readline().strip().split()
        cite = int(pub[0])

        assert 0 <=cite <=10**9
        assert len(pub[1:]) == arr[i], ' '.join([x for x in pub[1:]]) + ' ' + str(arr[i])
        assert len(list(set(pub[1:]))) == arr[i], ' '.join([x for x in list(set(pub[1:]))]) + ' ' + str(arr[i])

        for auth in pub[1:]:
            assert 1 <= len(auth) <= 10

    for i in range(q):
        auth = f_in.readline().strip()
        assert 1 <= len(auth) <= 10



if __name__ == "__main__":

    for i in range(1, 2):
        f_in = open("ex%d.txt"%i, 'r')
        comp(f_in, sys.stdout)


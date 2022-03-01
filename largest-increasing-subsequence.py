import sys


def largest_increasing_subsequence(sequence, n):
    D = [0] * n
    prev = [-1] * n

    for i in range(n):
        D[i] = 1
        for j in range(i):
            if sequence[i] > sequence[j] and D[i] < D[j] + 1:
                D[i] = D[j] + 1
                prev[i] = j

    max_elem = D[0]
    max_index = 0
    for idx, elem in enumerate(D):
        if max_elem < D[idx]:
            max_elem = D[idx]
            max_index = idx

    L = [-1] * max_elem
    j = max_index
    i = max_elem - 1
    while i >= 0:
        L[i] = sequence[j]
        j = prev[j]
        i -= 1
    return L


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))
    print(largest_increasing_subsequence(seq, n))

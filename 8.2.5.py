import sys


def largest_increasing_subsequence(sequence, n):
    D = [0] * n

    for i in range(n):
        D[i] = 1
        for j in range(i):
            if sequence[i] >= sequence[j] and sequence[i] % sequence[j] == 0 and D[i] < D[j] + 1:
                D[i] = D[j] + 1

    return max(D)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))
    print(largest_increasing_subsequence(seq, n))

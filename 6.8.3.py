import sys


def counting_sort(numbers, maximum):
    cnt = [0] * (maximum)
    for i in numbers:
        cnt[i - 1] += 1
    i = 0
    for j in range(maximum):
        while cnt[j] > 0:
            numbers[i] = str(j + 1)
            i += 1
            cnt[j] -= 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    counting_sort(numbers, max(numbers))
    print(' '.join(numbers))

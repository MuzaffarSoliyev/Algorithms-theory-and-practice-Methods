import sys


def binary_search(numbers, key):
    l = 0
    r = len(numbers) - 1
    while l <= r:
        middle = (r + l) // 2
        if numbers[middle] == key:
            return middle + 1
        elif numbers[middle] > key:
            r = middle - 1
        else:
            l = middle + 1
    return -1


if __name__ == '__main__':
    numbers = list(map(int, sys.stdin.readline().split()))
    numbers = numbers[1:]
    keys = list(map(int, sys.stdin.readline().split()))
    keys = keys[1:]
    for key in keys:
        print(binary_search(numbers, key), sep='', end=' ')

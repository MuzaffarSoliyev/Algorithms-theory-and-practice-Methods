import sys


def quick_sort(numbers, l, r):
    i = l
    j = r
    x = numbers[(l + r) // 2]
    while i <= j:
        while numbers[i] < x:
            i += 1
        while numbers[j] > x:
            j -= 1

        if i <= j:
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1
    if i < r:
        quick_sort(numbers, i, r)
    if l < j:
        quick_sort(numbers, l, j)


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, sys.stdin.readline().split()))
    quick_sort(numbers, 0, n - 1)
    print(numbers)

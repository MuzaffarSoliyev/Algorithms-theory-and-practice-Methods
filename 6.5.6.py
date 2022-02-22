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


def binary_search(numbers, key):
    l = 0
    r = len(numbers) - 1
    count = 0
    while l <= r:
        middle = (r + l) // 2
        if numbers[middle] == key:
            count += 1
            return middle + 1
        elif numbers[middle] > key:
            r = middle - 1
        else:
            l = middle + 1
    return -1

def solver1(point, arr):
    count = 0
    for i in arr:
        if i <= point:
            count += 1
    return count


def solver2(point, arr):
    count = 0
    for i in arr:
        if i < point:
            count += 1
    return count


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    sections_starts = []
    sections_ends = []
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        sections_starts.append(a)
        sections_ends.append(b)
    points = list(map(int, sys.stdin.readline().split()))

    quick_sort(sections_starts, 0, n - 1)
    quick_sort(sections_ends, 0, n - 1)
    results = []
    for point in points:
        n = solver1(point, sections_starts)
        m = solver1(point, sections_ends)
        results.append(str(n - m))
    print(" ".join(results))

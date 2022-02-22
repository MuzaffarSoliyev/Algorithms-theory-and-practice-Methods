import sys


def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    ptr1 = 0
    ptr2 = 0
    merged_arr = []
    for i in range(n + m):
        if ptr2 == m or (ptr1 < n and arr1[ptr1] < arr2[ptr2]):
            merged_arr.append(arr1[ptr1])
            ptr1 += 1
        else:
            merged_arr.append(arr2[ptr2])
            ptr2 += 1
    return merged_arr


def merge_sort(numbers, n):
    if n == 1:
        return numbers
    arr1 = [numbers[i] for i in range(n // 2)]
    arr2 = [numbers[i] for i in range(n // 2, n)]

    arr1 = merge_sort(arr1, len(arr1))
    arr2 = merge_sort(arr2, len(arr2))

    return merge(arr1, arr2)


if __name__ == '__main__':
    numbers = list(map(int, sys.stdin.readline().split()))
    print(merge_sort(numbers, len(numbers)))

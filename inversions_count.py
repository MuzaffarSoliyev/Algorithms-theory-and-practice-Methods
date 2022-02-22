import sys


def inversions(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    ptr1 = 0
    ptr2 = 0
    merged_array = []
    inversions = 0
    for i in range(n + m):
        if ptr2 == m or (ptr1 < n and arr1[ptr1] <= arr2[ptr2]):
            merged_array.append(arr1[ptr1])
            ptr1 += 1
        else:
            merged_array.append(arr2[ptr2])
            inversions += (n - ptr1)
            ptr2 += 1
    return merged_array, inversions


def inversions_count(numbers, n):
    if n == 1:
        return numbers, 0
    middle = len(numbers) // 2

    arr1, count_left = inversions_count(numbers[:middle], len(numbers[:middle]))
    arr2, count_right = inversions_count(numbers[middle:], len(numbers[middle:]))

    arr, count = inversions(arr1, arr2)

    return arr, (count_left + count_right + count)


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, sys.stdin.readline().split()))
    arr, count = inversions_count(numbers, len(numbers))
    print(count)

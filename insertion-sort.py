import sys


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
    return numbers


if __name__ == '__main__':
    numbers = list(map(int, sys.stdin.readline().split()))
    print(insertion_sort(numbers))

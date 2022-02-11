def fib_digit(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2, n + 1):
        arr.append((arr[i - 1] + arr[i - 2]) % 10)
    return arr[n]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()

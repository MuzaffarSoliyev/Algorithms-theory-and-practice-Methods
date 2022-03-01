import sys


def levenshtein_distance(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[-1] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for i in range(m + 1):
        dp[0][i] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diff = int(str1[i - 1] != str2[j - 1])
            dp[i][j] = min(dp[i - 1][j - 1] + diff, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
    print(dp[n][m])


if __name__ == '__main__':
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    levenshtein_distance(str1, str2)

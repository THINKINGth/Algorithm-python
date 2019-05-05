# DP (dynamic programming)问题


# 背包问题
def knapsack(w, v, i, j, n):
    if i == n:
        res = 0
    elif j < w[i]:
        res = knapsack(w, v, i + 1, j, n)
    else:
        res = max(knapsack(w, v, i + 1, j, n), knapsack(w, v, i + 1, j - w[i], n) + v[i])
    return res


# 背包问题（顺序）
def knapsacks(w, v, wmax):
    n = len(w)
    dp = [[0 for i in range(wmax + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(wmax + 1):
            if j < w[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])
    return dp[n][wmax]


# 背包问题（逆序）
def rev_knapsacks(w, v, wmax):
    n = len(w)
    dp = [[0 for i in range(wmax + 1)] for j in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(wmax + 1):
            if j < w[i]:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])
    return dp[0][wmax]


def _test():
    wmax = 5
    w = [2, 1, 3, 2]
    v = [3, 2, 4, 2]
    print(knapsack(w, v, 0, wmax, 4))
    print(knapsacks(w, v, wmax))
    print(rev_knapsacks(w, v, wmax))


_test()

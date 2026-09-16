class Solution:
    def numberOfSets(self, n, k):
        MOD = 1000000007

        dp = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(n):
                if i > 0:
                    prefix = (prefix + dp[i - 1][j - 1]) % MOD

                if i > 0:
                    dp[i][j] = dp[i - 1][j]

                dp[i][j] = (dp[i][j] + prefix) % MOD

        return dp[n - 1][k]
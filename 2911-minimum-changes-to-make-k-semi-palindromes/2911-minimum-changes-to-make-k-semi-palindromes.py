class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        for l in range(n):
            for r in range(l + 1, n):
                length = r - l + 1
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for offset in range(d):
                        group_len = (length - 1 - offset) // d + 1

                        for q in range(group_len // 2):
                            left = l + offset + q * d
                            right = l + offset + (group_len - 1 - q) * d

                            if s[left] != s[right]:
                                changes += 1

                    best = min(best, changes)

                cost[l][r] = best

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
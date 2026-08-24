class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        
        prefix = stones[:]

        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        ans = prefix[-1]

        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans
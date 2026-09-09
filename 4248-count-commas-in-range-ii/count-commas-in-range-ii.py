class Solution:
    def countCommas(self, n):
        ans = 0
        start = 1000

        while start <= n:
            ans += n - start + 1
            start *= 1000

        return ans
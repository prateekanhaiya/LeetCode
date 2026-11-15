
class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7

        even = 1
        odd = 0

        prefix = 0
        ans = 0

        for num in arr:
            prefix += num

            if prefix % 2 == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1

            ans %= MOD

        return ans

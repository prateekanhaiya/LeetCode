
class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        values = [0] * k

        for bit in range(32):
            count = 0

            for num in nums:
                if num & (1 << bit):
                    count += 1

            for i in range(min(count, k)):
                values[i] |= (1 << bit)

        answer = 0

        for value in values:
            answer = (answer + value * value) % MOD

        return answer

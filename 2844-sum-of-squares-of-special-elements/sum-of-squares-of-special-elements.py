
class Solution:
    def sumOfSquares(self, nums):
        n = len(nums)
        answer = 0

        for i in range(1, n + 1):
            if n % i == 0:
                answer += nums[i - 1] ** 2

        return answer

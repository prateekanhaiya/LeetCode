class Solution:
    def sumCounts(self, nums):
        answer = 0

        for i in range(len(nums)):
            distinct = set()

            for j in range(i, len(nums)):
                distinct.add(nums[j])
                answer += len(distinct) ** 2

        return answer

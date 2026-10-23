
class Solution:
    def sortPermutation(self, nums):
        misplaced = [nums[i] for i in range(len(nums)) if nums[i] != i]

        if not misplaced:
            return 0

        answer = misplaced[0]

        for num in misplaced[1:]:
            answer &= num

        return answer

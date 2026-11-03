class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(max(nums) - num for num in nums)
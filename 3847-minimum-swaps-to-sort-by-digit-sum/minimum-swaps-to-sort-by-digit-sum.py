
class Solution:
    def minSwaps(self, nums):
        def digit_sum(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        position = {value: i for i, value in enumerate(sorted_nums)}
        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i] or position[nums[i]] == i:
                continue

            length = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = position[nums[j]]
                length += 1

            swaps += length - 1

        return swaps

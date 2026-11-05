class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0

        for a in arr1:
            if all(abs(a - b) > d for b in arr2):
                count += 1

        return count
class Solution:
    def lexicographicallySmallestArray(self, nums, limit):

        n = len(nums)

        # (value, original index)
        arr = []

        for i in range(n):
            arr.append((nums[i], i))

        # Sort by value
        arr.sort()

        ans = nums[:]

        i = 0

        while i < n:

            j = i

            # Find one connected group
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Get indices and values of this group
            values = []
            indices = []

            for k in range(i, j + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            # Sort both
            values.sort()
            indices.sort()

            # Put smallest values at smallest indices
            for k in range(len(values)):
                ans[indices[k]] = values[k]

            i = j + 1

        return ans
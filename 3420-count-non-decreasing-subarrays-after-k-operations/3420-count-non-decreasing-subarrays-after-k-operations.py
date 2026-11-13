
class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        LOG = n.bit_length()

        jump = [nxt]
        weight = [[(nxt[i] - i) * nums[i] for i in range(n)]]

        for j in range(1, LOG):
            pj = jump[-1]
            pw = weight[-1]

            nj = [n] * n
            nw = [0] * n

            for i in range(n):
                mid = pj[i]

                if mid < n:
                    nj[i] = pj[mid]
                    nw[i] = pw[i] + pw[mid]
                else:
                    nw[i] = pw[i]

            jump.append(nj)
            weight.append(nw)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Calculate the sum of prefix maximums
        def get_max_sum(l, r):
            pos = l
            total = 0

            for j in range(LOG - 1, -1, -1):
                nxt_pos = jump[j][pos]

                if nxt_pos <= r:
                    total += weight[j][pos]
                    pos = nxt_pos

            total += (r - pos + 1) * nums[pos]

            return total

        ans = 0
        left = 0

        # Sliding window
        for r in range(n):

            while left <= r:
                total = get_max_sum(left, r)
                original = prefix[r + 1] - prefix[left]

                operations = total - original

                if operations <= k:
                    break

                left += 1

            ans += r - left + 1

        return ans

class Solution:
    def maxDepthAfterSplit(self, seq):
        ans = []
        depth = 0

        for ch in seq:
            if ch == '(':
                depth += 1

            ans.append(depth % 2)

            if ch == ')':
                depth -= 1

        return ans
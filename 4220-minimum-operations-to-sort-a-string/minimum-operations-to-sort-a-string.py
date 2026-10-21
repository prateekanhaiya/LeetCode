
class Solution:
    def minOperations(self, s):
        if s == ''.join(sorted(s)):
            return 0

        if len(s) == 2:
            return -1

        if s[0] == min(s) or s[-1] == max(s):
            return 1

        if (s[0] == max(s) and s.count(s[0]) == 1 and
                s[-1] == min(s) and s.count(s[-1]) == 1):
            return 3

        return 2

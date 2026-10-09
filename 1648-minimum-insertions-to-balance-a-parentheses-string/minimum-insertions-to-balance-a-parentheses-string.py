
class Solution:
    def minInsertions(self, s):
        open_count = 0
        answer = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open_count += 1
                i += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    answer += 1
                    i += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    answer += 1

        answer += open_count * 2
        return answer
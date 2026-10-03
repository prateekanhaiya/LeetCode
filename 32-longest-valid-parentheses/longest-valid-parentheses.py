class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        answer = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    answer = max(answer, i - stack[-1])

        return answer
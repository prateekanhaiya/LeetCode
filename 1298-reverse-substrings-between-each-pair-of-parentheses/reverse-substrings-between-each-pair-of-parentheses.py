class Solution:
    def reverseParentheses(self, s):
        stack = []

        for ch in s:
            if ch == ')':
                temp = []

                while stack[-1] != '(':
                    temp.append(stack.pop())

                stack.pop()

                for char in temp:
                    stack.append(char)
            else:
                stack.append(ch)

        return ''.join(stack)
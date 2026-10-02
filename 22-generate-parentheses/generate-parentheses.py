class Solution:
    def generateParenthesis(self, n):
        answer = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                answer.append(current)
                return

            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack("", 0, 0)

        return answer
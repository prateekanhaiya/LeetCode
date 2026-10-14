
class Solution:
    def maxSumOfSquares(self, num, sum):
        if sum > num * 9:
            return ""

        answer = []

        while sum >= 9:
            answer.append('9')
            sum -= 9

        if sum > 0:
            answer.append(str(sum))

        answer.extend(['0'] * (num - len(answer)))

        return ''.join(answer)

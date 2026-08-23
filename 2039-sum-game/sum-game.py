class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        diff = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                diff -= int(num[i])

        # Odd number of '?' means Alice can always win
        if (left_q + right_q) % 2 == 1:
            return True

        # Expected difference that '?' can create
        diff += (left_q - right_q) * 9 // 2

        return diff != 0
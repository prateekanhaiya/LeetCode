
class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, length, value):
            squares[node] = (
                squares[node] + 2 * value * total[node]
                + value * value * length
            ) % MOD
            total[node] = (total[node] + value * length) % MOD
            lazy[node] += value

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, right - left + 1, 1)
                return

            mid = (left + right) // 2

            if lazy[node]:
                apply(node * 2, mid - left + 1, lazy[node])
                apply(node * 2 + 1, right - mid, lazy[node])
                lazy[node] = 0

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            total[node] = (total[node * 2] + total[node * 2 + 1]) % MOD
            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        last = {}
        answer = 0

        for i, value in enumerate(nums):
            prev = last.get(value, -1)
            update(1, 0, n - 1, prev + 1, i)
            answer = (answer + squares[1]) % MOD
            last[value] = i

        return answer

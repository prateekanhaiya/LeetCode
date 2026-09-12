class Solution:
    def maximumWeight(self, intervals):
        from bisect import bisect_left

        n = len(intervals)

        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append((r, l, w, i))

        arr.sort()
        ends = [x[0] for x in arr]

        dp = [[None] * (n + 1) for _ in range(5)]

        for i in range(n + 1):
            dp[0][i] = (0, ())

        for k in range(1, 5):
            for i in range(1, n + 1):
                best = dp[k][i - 1]

                r, l, w, idx = arr[i - 1]
                p = bisect_left(ends, l)

                if dp[k - 1][p] is not None:
                    old_score, old_indices = dp[k - 1][p]
                    new_score = old_score + w
                    new_indices = tuple(sorted(old_indices + (idx,)))

                    candidate = (new_score, new_indices)

                    if best is None:
                        best = candidate
                    elif candidate[0] > best[0]:
                        best = candidate
                    elif candidate[0] == best[0] and candidate[1] < best[1]:
                        best = candidate

                dp[k][i] = best

        answer = (0, ())

        for k in range(1, 5):
            current = dp[k][n]

            if current is None:
                continue

            if current[0] > answer[0]:
                answer = current
            elif current[0] == answer[0] and current[1] < answer[1]:
                answer = current

        return list(answer[1])
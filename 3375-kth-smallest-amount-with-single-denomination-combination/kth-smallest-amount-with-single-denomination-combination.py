from itertools import combinations

class Solution:
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for r in range(1, len(coins) + 1):
                for group in combinations(coins, r):
                    L = 1

                    for c in group:
                        L = lcm(L, c)

                        if L > x:
                            break

                    if L <= x:
                        if r % 2 == 1:
                            total += x // L
                        else:
                            total -= x // L

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
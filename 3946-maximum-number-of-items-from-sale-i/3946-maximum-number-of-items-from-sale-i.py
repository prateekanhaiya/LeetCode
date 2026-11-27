
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        value = [x + 1 for x in free]
        min_price = min(price for factor, price in items)

        if budget < min_price:
            return 0

        dp0 = [-10**9] * (budget + 1)
        dp1 = [-10**9] * (budget + 1)

        dp0[0] = 0

        for i in range(n):
            factor, price = items[i]

            for b in range(budget, price - 1, -1):
                if price == min_price:
                    dp1[b] = max(
                        dp1[b],
                        dp0[b - price] + value[i],
                        dp1[b - price] + value[i]
                    )
                else:
                    dp0[b] = max(
                        dp0[b],
                        dp0[b - price] + value[i]
                    )

                    dp1[b] = max(
                        dp1[b],
                        dp1[b - price] + value[i]
                    )

        ans = 0

        for b in range(budget + 1):
            if dp1[b] >= 0:
                ans = max(ans, dp1[b] + (budget - b) // min_price)

            if budget - b < min_price and dp0[b] >= 0:
                ans = max(ans, dp0[b])

        return ans

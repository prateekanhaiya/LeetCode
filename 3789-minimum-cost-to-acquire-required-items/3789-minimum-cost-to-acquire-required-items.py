
class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        separate = need1 * cost1 + need2 * cost2

        common = min(need1, need2)

        mixed = (common * costBoth +
                 (need1 - common) * cost1 +
                 (need2 - common) * cost2)

        all_both = max(need1, need2) * costBoth

        return min(separate, mixed, all_both)

import heapq

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]
            bit >>= 1

        return idx + 1


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        fw = Fenwick(k)

        for i in range(1, k + 1):
            fw.update(i, 1)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            while busy and busy[0][0] <= arrival[i]:
                finish, server = heapq.heappop(busy)
                fw.update(server + 1, 1)

            total = fw.query(k)

            if total == 0:
                continue

            start = i % k
            before = fw.query(start)

            if before < total:
                server = fw.kth(before + 1) - 1
            else:
                server = fw.kth(1) - 1

            fw.update(server + 1, -1)
            count[server] += 1

            heapq.heappush(busy, (arrival[i] + load[i], server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
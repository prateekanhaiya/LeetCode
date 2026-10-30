
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, 1)]
        dist = {}

        while pq:
            cost, node, count = heapq.heappop(pq)

            if node == n - 1:
                return cost

            if (node, count) in dist:
                continue

            dist[(node, count)] = cost

            for nxt, weight in graph[node]:
                new_count = count + 1 if labels[nxt] == labels[node] else 1

                if new_count <= k and (nxt, new_count) not in dist:
                    heapq.heappush(pq, (cost + weight, nxt, new_count))

        return -1

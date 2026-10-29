
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                up[0][u] = u if p == -1 else p

                if p != -1:
                    depth[u] = depth[p] + 1
                    pref[u] = pref[p] ^ (1 << (ord(s[u]) - 97))
                else:
                    pref[u] = 1 << (ord(s[u]) - 97)

                for j in range(1, LOG):
                    up[j][u] = up[j - 1][up[j - 1][u]]

                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        bit = [0] * (n + 2)

        def add(i, value):
            while i < len(bit):
                bit[i] ^= value
                i += i & -i

        def update_subtree(u, value):
            add(tin[u] + 1, value)
            add(tout[u] + 2, value)

        def get_prefix(i):
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def get_mask(u):
            return pref[u] ^ get_prefix(tin[u] + 1)

        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                old_mask = 1 << (ord(chars[u]) - 97)
                new_mask = 1 << (ord(c) - 97)

                if old_mask != new_mask:
                    update_subtree(u, old_mask ^ new_mask)
                    chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                ancestor = lca(u, v)

                mask = get_mask(u) ^ get_mask(v) ^ (1 << (ord(chars[ancestor]) - 97))
                answer.append((mask & (mask - 1)) == 0)

        return answer
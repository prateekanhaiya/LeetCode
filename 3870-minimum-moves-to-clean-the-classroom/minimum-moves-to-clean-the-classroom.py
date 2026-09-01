import collections

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])
        start_r = -1
        start_c = -1
        litters = []

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_r, start_c = i, j
                elif classroom[i][j] == 'L':
                    litters.append((i, j))

        k = len(litters)
        if k == 0:
            return 0

        target_mask = (1 << k) - 1
        litter_idx = {pos: idx for idx, pos in enumerate(litters)}

        max_energy_left = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]

        queue = collections.deque([(start_r, start_c, 0, energy, 0)])
        max_energy_left[start_r][start_c][0] = energy
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, mask, e, steps = queue.popleft()

            if mask == target_mask:
                return steps

            if e == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    cell = classroom[nr][nc]
                    next_e = energy if cell == 'R' else e - 1

                    next_mask = mask
                    if cell == 'L' and (nr, nc) in litter_idx:
                        next_mask |= 1 << litter_idx[(nr, nc)]

                    if next_e > max_energy_left[nr][nc][next_mask]:
                        max_energy_left[nr][nc][next_mask] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))

        return -1
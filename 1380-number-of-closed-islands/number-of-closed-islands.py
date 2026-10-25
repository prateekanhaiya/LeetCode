
class Solution(object):
    def closedIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    stack = [(r, c)]
                    grid[r][c] = 1
                    closed = True

                    while stack:
                        x, y = stack.pop()

                        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                            closed = False

                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx = x + dx
                            ny = y + dy

                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                                grid[nx][ny] = 1
                                stack.append((nx, ny))

                    if closed:
                        count += 1

        return count
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if not grid or grid[0][0] == 1:
            return -1
        n = len(grid)
        return self.bfs(n, grid)

    def bfs(self, n, grid):
        my_queue = collections.deque()
        my_queue.append((grid[0][0], 1, 0, 0))
        while my_queue:
            value, depth, row, col = my_queue.popleft()
            if row == (n - 1) and col == (n - 1):
                return depth
            for x, y in self.adjacent(row, col, n, grid):
                if grid[x][y] == 0:
                    my_queue.append((grid[x][y], depth + 1, x, y))
                    grid[x][y] = 1

        return -1

    def adjacent(self, row, col, n, grid):
        for r, c in ((row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1),
                     (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if 0 <= r < n and 0 <= c < n and not grid[r][c]:
                yield (r, c)


if __name__ == '__main__':
    # grid = [[0, 1], [1, 0]]
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    # grid = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
    print(Solution().shortestPathBinaryMatrix(grid))

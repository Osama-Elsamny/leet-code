from collections import deque


class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return -1
        if not grid[0]:
            return -1
        counter = 0
        row_len = len(grid)
        col_len = len(grid[0])
        my_queue = deque()
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    my_queue.append((i, j, 0))
                elif val == 1:
                    counter += 1

        depth = 0
        while my_queue:
            row, col, depth = my_queue.popleft()
            for a_row, a_col in self.adjacent(row, col, row_len, col_len):
                if grid[a_row][a_col] == 1:
                    grid[a_row][a_col] = 2
                    my_queue.append((a_row, a_col, depth + 1))
                    counter -= 1

        return depth if counter == 0 else -1

    def adjacent(self, row, col, row_len, col_len):
        my_list = []
        for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if 0 <= r < row_len and 0 <= c < col_len:
                my_list.append((r, c))
        return my_list


if __name__ == '__main__':
    # grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    grid = [[0, 2]]
    print(Solution().orangesRotting(grid))

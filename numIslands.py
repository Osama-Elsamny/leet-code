class Solution:
    def numIslands(self, grid):
        counter = 0
        row_length = len(grid)
        for row in range(row_length):
            col_lenth = len(grid[row])
            for col in range(col_lenth):
                if grid[row][col] == '1':
                    self.dfs(row, col, grid, col_lenth, row_length)
                    counter += 1
        return counter

    def dfs(self, row, col, grid, col_lenth, row_length):
        if row < 0 or col < 0 or col > col_lenth - 1 or row > row_length - 1:
            return
        if grid[row][col] == '0':
            return
        grid[row][col] = '0'
        self.dfs(row - 1, col, grid, col_lenth, row_length)
        self.dfs(row, col - 1, grid, col_lenth, row_length)
        self.dfs(row + 1, col, grid, col_lenth, row_length)
        self.dfs(row, col + 1, grid, col_lenth, row_length)


if __name__ == '__main__':
    test = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    grid = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]
    grid2 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    print(Solution().numIslands(test))

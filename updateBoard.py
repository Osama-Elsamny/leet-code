import collections


class Solution:
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        self.bfs(board, click)
        return board

    def bfs(self, board, click):
        my_queue = collections.deque()
        my_queue.append((board[click[0]][click[1]], click[0], click[1]))

        while my_queue:
            cell, x, y = my_queue.popleft()
            count = 0
            current_list = []
            for r, c in self.adjacent(x, y, board):
                if board[r][c] == 'B':
                    continue
                elif board[r][c] == 'E':
                    current_list.append((board[r][c], r, c))
                elif board[r][c] == 'M':
                    count += 1
            if count != 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                my_queue.extend(current_list)

    def adjacent(self, row, col, grid):
        row_len = len(grid)
        col_len = len(grid[0])
        for r, c in ((row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1),
                     (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
            if 0 <= r < row_len and 0 <= c < col_len:
                yield (r, c)

    def updateBoard(self, board, click):
        EMPTY = "E"
        MINE = "M"
        BLANK = "B"
        BOOM = "X"
        n = len(board)
        if n == 0:
            return board
        m = len(board[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        queue = collections.deque()
        queue.append(click)
        while queue:
            row, col = queue.popleft()

            if board[row][col] == MINE:
                board[row][col] = BOOM
                return board
            elif board[row][col] == EMPTY:
                mines = []
                count = 0
                for d in DIRECTIONS:
                    r = row + d[0]
                    c = col + d[1]

                    if r < 0 or c < 0 or r >= n or c >= m or (board[r][c] != EMPTY and board[r][c] != MINE):
                        continue
                    elif board[r][c] == MINE:
                        count += 1
                    mines.append([r, c])
                if count == 0:
                    board[row][col] = BLANK
                    queue.extend(mines)
                else:
                    board[row][col] = str(count)

        return board


if __name__ == '__main__':
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]

    click = [3, 0]
    print(Solution().updateBoard(board, click))

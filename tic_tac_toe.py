class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row_score = [0 for _ in range(n)]
        self.col_score = [0 for _ in range(n)]
        self.dig_score = 0
        self.rev_dig_score = 0
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        player = -1 if player == 2 else player
        self.row_score[row] += player
        self.col_score[col] += player
        if row == col:
            self.dig_score += player
        if row == (self.n - 1 - col):
            self.rev_dig_score += player

        if abs(self.row_score[row]) == self.n or abs(self.col_score[col]) == self.n or abs(self.dig_score) == self.n or abs(
                self.rev_dig_score) == self.n:
            player = 2 if player == -1 else player
            return player
        return 0


if __name__ == '__main__':
    test = TicTacToe(3)
    test.move(1, 2, 5)
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

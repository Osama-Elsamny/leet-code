import collections


class Solution:
    def snakesAndLadders(self, board):
        if not board:
            return -1
        board_len = len(board)
        destination = board_len * board_len
        my_queue = collections.deque([1])
        my_map = {1: 0}
        while my_queue:
            s = my_queue.popleft()

            if s == destination:
                return my_map[s]
            end = s + 6 if s + 6 < destination else destination
            for s2 in range(s + 1, end + 1):
                r, c = self.get_row_col(s2, board_len)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in my_map:
                    my_map[s2] = my_map[s] + 1
                    my_queue.append(s2)

        return -1

    def get_row_col(self, s, board_len):
        # the rem is its place in the array
        rem = (s - 1) % board_len
        # the quot is it filliped array or not
        quot = (s - 1) // board_len
        row = board_len - 1 - quot
        col = rem if row % 2 != board_len % 2 else board_len - 1 - rem

        return row, col


if __name__ == '__main__':
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]]

    # print(Solution().snakesAndLadders(board))

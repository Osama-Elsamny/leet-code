aclass Solution:
    def prisonAfterNDays(self, cells, N):
        my_map = {}
        while N > 0:
            hashable = tuple(cells)
            if hashable in my_map:
                N = N % (my_map[hashable] - N)
            my_map[hashable] = N
            if N >= 1:
                N -= 1
                cells = self.one_day_pass(cells)
        return cells

    def one_day_pass(self, cells):
        new_cells = 8 * [0]
        new_cells[0] = 0
        new_cells[7] = 0
        for i in range(1, 7):
            new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
        return new_cells


if __name__ == '__main__':
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    N = 7
    print(Solution().prisonAfterNDays(cells, N))

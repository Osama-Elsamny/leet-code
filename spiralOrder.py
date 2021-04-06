class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        row_len = len(matrix)
        col_len = len(matrix[0])
        k = 0
        j = 0
        res = []
        while k < row_len and j < col_len:
            #  Adding the top row_len row
            for i in range(j, col_len):
                res.append(matrix[k][i])
            k += 1
            for i in range(k, row_len):
                res.append(matrix[i][col_len - 1])
            col_len -= 1
            if k < row_len:
                for i in range(col_len - 1, j - 1, -1):
                    res.append(matrix[row_len - 1][i])
                row_len -= 1

            if j < col_len:
                for i in range(row_len - 1, k - 1, -1):
                    res.append(matrix[i][j])
                j += 1
        return res


if __name__ == '__main__':
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))

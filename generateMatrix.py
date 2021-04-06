class Solution:
    def generateMatrix(self, n):
        # result = []
        # for i in range(1, n + 1):
        #     j = n * i
        #     if i % 2 == 0:
        #         result.append([k for k in range(j, ((i - 1) * n), -1)])
        #     else:
        #         result.append([k for k in range(((i - 1) * n) + 1, j + 1)])
        # print(result)
        result = [[0 for _ in range(n)] for _ in range(n)]
        k = 0
        colItr = 0
        num = 1
        colEnd = n
        rowEnd = n

        while k < rowEnd and colItr < colEnd and num <= n ** 2:
            for i in range(colItr, n):
                result[k][i] = num
                num += 1
            k += 1
            for i in range(k, rowEnd):
                result[i][colEnd - 1] = num
                num += 1
            colEnd -= 1

            if k < rowEnd:
                for i in range(colEnd - 1, colItr - 1, -1):
                    result[rowEnd - 1][i] = num
                    num += 1
                rowEnd -= 1

            if colItr < colEnd:
                for i in range(rowEnd - 1, k - 1, -1):
                    result[i][colItr] = num
                    num += 1
                colItr += 1

        print(result)


if __name__ == '__main__':
    Solution().generateMatrix(3)

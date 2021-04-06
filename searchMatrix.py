from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # O(m log n solution)
        # if not matrix or not matrix[0]:
        #     return False
        # col_length = len(matrix)
        # row_length = len(matrix[0])
        # for i in range(col_length):
        #     if self.binarySearch(matrix[i], 0, row_length - 1, target):
        #         return True
        # return False

        # O(m +n) solution
        if not matrix or not matrix[0]:
            return False
        col_length = len(matrix)
        row_length = len(matrix[0])
        row = row_length - 1
        col = 0
        while col < col_length and row >= 0:
            if matrix[col][row] == target:
                return True
            elif target < matrix[col][row]:
                row -= 1
            else:
                col += 1
        return False

    def binarySearch(self, arr, left, right, elem):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == elem:
                return True
            elif arr[mid] > elem:
                right = mid - 1
            elif arr[mid] < elem:
                left = mid + 1
        return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(Solution().searchMatrix(matrix, 25))

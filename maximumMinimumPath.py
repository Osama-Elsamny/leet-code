import heapq


class Solution:
    def maximumMinimumPath(self, A):
        if not A:
            return None
        if not A[0]:
            return None
        row = len(A)
        col = len(A[0])
        heap = [(-A[row - 1][col - 1], row - 1, col - 1)]
        A[row - 1][col - 1] = -1
        score = A[0][0]
        heapq.heapify(heap)
        while heap:
            s, i, j = heapq.heappop(heap)
            score = min(-s, score)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if not (x or y):
                    return score
                if 0 <= x < row and 0 <= y < col and A[x][y] >= 0:
                    heapq.heappush(heap, (-A[x][y], x, y))
                A[x][y] = -1

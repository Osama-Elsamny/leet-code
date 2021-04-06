import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stones = [-num for num in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            x = -1 * x
            y = -1 * y
            if x != y:
                z = abs(x - y)
                heapq.heappush(stones, -z)
        return -1 * heapq.heappop(stones)


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(stones))

import heapq


class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        result = 0
        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            result += stick1 + stick2
            heapq.heappush(sticks, stick1 + stick2)
        return result


if __name__ == '__main__':
    sticks = [2, 4, 3]
    print(Solution().connectSticks(sticks))

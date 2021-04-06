import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        rooms_list = []
        heapq.heappush(rooms_list, intervals[0][1])
        for i in intervals[1:]:
            if rooms_list[0] <= i[0]:
                heapq.heappop(rooms_list)
            heapq.heappush(rooms_list, i[1])
        return len(rooms_list)


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    # intervals = [[7, 10], [2, 4]]
    # intervals = [[9, 10], [4, 9], [4, 17]]
    # intervals = [[1, 5], [8, 9], [8, 9]]
    print(Solution().minMeetingRooms(intervals))

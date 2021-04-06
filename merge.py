class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = [intervals[0]]
        current_interval = 0
        for n in intervals[1:]:
            if res[current_interval][0] <= n[0] <= res[current_interval][1]:
                res[current_interval][1] = n[1] if n[1] > res[current_interval][1] else res[current_interval][1]
            else:
                res.append(n)
                current_interval += 1
        return res


if __name__ == '__main__':
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4], [1, 4]]
    intervals = [[1, 4], [2, 3]]
    print(Solution().merge(intervals))

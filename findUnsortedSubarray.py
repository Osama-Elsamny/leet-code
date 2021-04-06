class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        num_len = len(nums)
        # cache = {}
        # cache[0] = 1
        # for i in range(1, num_len):
        #     cache[i] = cache[i - 1] + 1 if nums[i] > nums[i - 1] else 1
        # return max(cache.values())

        # First Try
        # start_index = 0
        # end_index = num_len - 1
        # while start_index < num_len:
        #     if nums[start_index] > nums[start_index + 1]:
        #         break
        #     start_index += 1
        # if start_index >= end_index:
        #     return 0
        # while end_index > 0:
        #     if nums[end_index] < nums[end_index - 1]:
        #         break
        #     end_index -= 1
        # return end_index - start_index + 1

        # Second try
        s = e = -1
        n, mx, mn = len(nums), float('-inf'), float('inf')
        for i in range(n):
            mx = max(mx, nums[i])
            if nums[i] < mx:
                e = i
        for i in range(n - 1, -1, -1):
            mn = min(mn, nums[i])
            if nums[i] > mn:
                s = i
        return e - s + 1 if s >= 0 else 0


if __name__ == '__main__':
    # print(Solution().findUnsortedSubarray([10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]))
    # print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(Solution().findUnsortedSubarray([1, 3, 2, 2, 2]))
    print(Solution().findUnsortedSubarray([1, 2, 3, 3, 3]))

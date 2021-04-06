class Solution:
    def find132pattern(self, nums):

        # O(nlog(n)) Binary Search
        # if not nums:
        #     return False
        # my_tuple = [(value, index) for index, value in enumerate(nums)]
        # sorted_nums = sorted(my_tuple)
        # small_left = nums[0]
        # for i in range(1, len(nums) - 1):
        #     if self.checkIf132Pattern(nums[i], small_left, i, sorted_nums):
        #         return True
        #     small_left = small_left if small_left < nums[i] else nums[i]
        # return False
        if not nums:
            return False
        nums_length = len(nums)
        min_so_far = [nums[0]]
        my_stack = []
        for i in range(1, nums_length):
            min_so_far.append(nums[i] if min_so_far[i - 1] > nums[i] else min_so_far[i - 1])

        for i in range(nums_length - 1, -1, -1):
            if nums[i] > min_so_far[i]:
                """
                min_so_far[i] >= my_stack[-1]: not nums[i] <= my_stack[-1]
                because we are sure that if is smaller than the minimum so far that
                there is no way we can use it. For example, if min so far is 6
                and my number is the stack is 5 and number that i on is 7
                """
                while my_stack and min_so_far[i] >= my_stack[-1]:
                    my_stack.pop()
                if my_stack and nums[i] > my_stack[-1]:
                    return True
                my_stack.append(nums[i])
        return False

    def checkIf132Pattern(self, greater, small_left, greater_index, sorted_nums):
        return self.binarySearch(sorted_nums, 0, len(sorted_nums) - 1, greater, small_left, greater_index)

    def binarySearch(self, arr, left, right, greater, smaller, smaller_index):
        while left <= right:
            mid = left + (right - left) // 2
            if smaller < arr[mid][0] < greater:
                if arr[mid][1] <= smaller_index:
                    left = mid + 1
                else:
                    return True
            elif arr[mid][0] >= greater:
                right = mid - 1
            elif arr[mid][0] <= smaller:
                left = mid + 1
        return False


if __name__ == '__main__':
    nums = [1, 3, 4, 2]
    print(Solution().find132pattern(nums))

import sys


class Solution:
    def maxSubArray(self, nums) -> int:
        largest_sum = -1 * sys.maxsize - 1
        length = len(nums)
        for left in range(length):
            runningWindow = 0
            for right in range(left, length):
                runningWindow += nums[right]
                largest_sum = max(runningWindow, largest_sum)
        return largest_sum

    def maxSubArrayDynamicPrograming(self, nums):
        largest_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            largest_sum = max(current_sum, largest_sum)
        return largest_sum

    def maxSubArrayDynamicFaster(self, nums):
        largest_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = current_sum + num if current_sum + num > num else num
            largest_sum = current_sum if current_sum > largest_sum else largest_sum
        return largest_sum


if __name__ == '__main__':
    # print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArrayDynamicPrograming([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArrayDynamicPrograming([-2, 1]))
    print(Solution().maxSubArrayDynamicPrograming([1, 2]))

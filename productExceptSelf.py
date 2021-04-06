class Solution:
    def productExceptSelf(self, nums):
        nums_length = len(nums)
        res = [num for num in nums]
        prev = next_item = 1
        for i in range(nums_length):
            temp = nums[i]
            if i != 0:
                nums[i] = prev * nums[i - 1]
            if i == 0:
                nums[i] = 1
            prev = temp

        for i in range(nums_length - 1, -1, -1):
            temp = res[i]
            if i != nums_length - 1:
                res[i] = next_item * res[i + 1]
            if i == nums_length - 1:
                res[nums_length - 1] = 1
            next_item = temp

        for i in range(nums_length):
            res[i] = res[i] * nums[i]

        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))

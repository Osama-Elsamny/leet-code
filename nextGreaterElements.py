class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        nums_len = len(nums)
        my_stack = []
        res = [-1] * nums_len
        for i in range(nums_len * 2):
            while my_stack and nums[my_stack[-1]] < nums[i % nums_len]:
                res[my_stack.pop()] = nums[i % nums_len]
            if i < nums_len:
                my_stack.append(i)
        return res


if __name__ == '__main__':
    nums = [1, 2, 1]
    print(Solution().nextGreaterElements(nums))

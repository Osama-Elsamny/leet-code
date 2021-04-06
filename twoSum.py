class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # enum_nums = enumerate(nums)
        # h = {}
        # for i, e in enum_nums:
        #     friend = target - e
        #     if friend not in h:
        #         h[e] = i
        #     else:
        #         return [h[friend], i]

        h = {}
        i = 0
        for num in nums:
            friend = target - num
            if friend not in h:
                h[num] = i
            else:
                return [h[friend], i]
            i += 1

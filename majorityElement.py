class Solution:
    def majorityElement(self, nums):
        # prev_counts = []
        # map_te = {}
        # set_nums = set(nums)
        # for num in set_nums:
        #     curr_count = nums.count(num)
        #     prev_counts.append(curr_count)
        #     map_te[curr_count] = num
        # return map_te[max(prev_counts)]

        ## I think a better way
        map_te = {}
        set_nums = set(nums)
        for num in set_nums:
            curr_count = nums.count(num)
            map_te[curr_count] = num
        return map_te[max(map_te.keys())]


if __name__ == '__main__':
    print(Solution().majorityElement([3, 2, 3]))

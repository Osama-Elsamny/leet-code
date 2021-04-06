class Solution:
    def rob(self, nums) -> int:
        cache = {}

        for i in range(len(nums)):
            house_chosen = nums[i] + cache[i - 2]
            house_not_chosen = cache[i]
            cache[i] = max(house_chosen, house_not_chosen)
        return max(cache)


if __name__ == '__main__':
    print(Solution().rob([1, 2]))

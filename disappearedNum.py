class Solution:
    def findDisappearedNumbers(self, nums):
        for n in nums: 
            nums[abs(n) - 1] = - abs(nums[abs(n) - 1])
        print("nums after for loop: {}".format(nums))
        return [i + 1 for i, n in enumerate(nums) if n > 0]



if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1,5]
    obj = Solution()
    test = obj.findDisappearedNumbers(nums)
    print("End of the program nums: {}".format(test))
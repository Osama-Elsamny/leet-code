import math


class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        if lenth == k or lenth == 0 or k == 0:
            return

        s = self.lcm(lenth, k) / k
        offset = 0
        temp = nums[0]
        for i in range(1, lenth + 1):
            step = ((i * k) + offset) % lenth
            temp, nums[step] = nums[step], temp
            if i % s == 0:
                offset += 1
                temp = nums[(step + 1) % lenth]

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def gcd(self, a, b):
        """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
        while b:
            a, b = b, a % b
        return a


if __name__ == '__main__':
    test = [1, 2, 3, 4]
    k = 2
    Solution().rotate(test, k)
    print(test)

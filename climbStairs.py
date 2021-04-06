class Solution:
    def climbStairs(self, n: int) -> int:
        return self.loopClimbStairs(n)

    def loopClimbStairs(self, n):
        array = {}
        array[0] = 1
        array[1] = 1
        for i in range(2, n + 1):
            array[i] = array[i - 1] + array[i - 2]
        return array[n]


if __name__ == '__main__':
    print(Solution().climbStairs(5))

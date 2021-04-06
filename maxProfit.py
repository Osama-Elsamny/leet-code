from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution one O(n^2)
        # gap = [0]len
        # lenn = len(prices)
        # for i in range(lenn):
        #     buy_price = prices[i]
        #     for j in range(i + 1, lenn):
        #         profit = prices[j] - buy_price
        #         if profit < 0:
        #             continue
        #         gap.append(profit)
        # print(gap)
        # return max(gap)
        # Solution two
        lenn = len(prices)
        if lenn == 0:
            return 0
        min_val = prices[0]
        profit = 0
        for i in range(lenn):
            cur_val = prices[i]
            if cur_val < min_val:
                min_val = cur_val
            elif cur_val - min_val > profit:
                profit = cur_val - min_val
        return profit


if __name__ == '__main__':
    out = Solution().maxProfit([100, 180, 260, 310, 40, 535, 695])
    print('out: {}'.format(out))

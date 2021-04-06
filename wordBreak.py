class Solution:
    # 2-d Solution
    # s_length = len(s)
    # matrix = [[False for _ in range(s_length)] for _ in range(s_length)]
    #
    # for l in range(1, s_length + 1):
    #     for i in range(s_length - l + 1):
    #         j = i + l - 1
    #         if s[i:j + 1] in wordDict:
    #             matrix[i][j] = True
    #             continue
    #         for k in range(i + 1, j + 1):
    #             if matrix[i][k - 1] and matrix[k][j]:
    #                 matrix[i][j] = True
    #                 break
    # return matrix[0][s_length - 1]
    def wordBreak(self, s, wordDict):
        s_length = len(s)
        dp = [False for _ in range(s_length+1)]
        dp[0] = True
        for l in range(1, s_length + 1):
            for i in range(l):
                if dp[i] and s[i:l] in wordDict:
                    dp[l] = True
                    break

        return dp[s_length]


if __name__ == '__main__':
    # s = "Iamace"
    # wordDict = ["I", "am", "ace", "a"]
    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "code"
    # wordDict = ["od", "x", "f", "c"]
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))

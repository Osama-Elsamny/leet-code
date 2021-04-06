class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth = len(s)
        if lenth == 0:
            return ''
        right = left = 0
        for i in range(lenth):
            len_odd = self.expand(s, i, i)
            len_even = self.expand(s, i, i + 1)
            max_len = max(len_even, len_odd)
            if max_len > right - left:
                right = i + max_len // 2
                left = i - (max_len-1) // 2
        return s[left:right + 1]

    def expand(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] == string[right]:
                left -= 1
                right += 1
            else:
                break
        return right - left - 1


if __name__ == '__main__':
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))

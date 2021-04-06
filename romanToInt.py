class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
        x = 0
        for i in range(len(s)):
            if i > 0 and values[s[i]] > values[s[i - 1]]:
                x += values[s[i]] - 2 * values[s[i - 1]]
            else:
                x += values[s[i]]
        return x
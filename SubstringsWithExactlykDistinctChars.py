class Solution:
    def __init__(self):
        self.my_counter = {}

    def substringsWithKDistinctChars(self, s, k):
        s_length = len(s)
        overage = 0
        result = set()
        for j in range(k):
            overage = self.add_to_counter(s[j], overage)

        for i in range(s_length - k + 1):
            if overage == 0:
                result.add(s[i:i + k])
            if i + k < s_length:
                overage = self.remove_from_counter(s[i], overage)
                overage = self.add_to_counter(s[i + k], overage)
        print(result)
        print(len(result))

    def remove_from_counter(self, item, overage):
        if self.my_counter[item] > 1:
            self.my_counter[item] -= 1
            overage -= 1
        else:
            del self.my_counter[item]

        return overage

    def add_to_counter(self, item, overage):
        if item in self.my_counter:
            self.my_counter[item] += 1
            overage += 1
        else:
            self.my_counter[item] = 1
        return overage


if __name__ == '__main__':
    s = "awaglknagawunagwkwagl"
    k = 4
    Solution().substringsWithKDistinctChars(s, k)

class Solution:
    def groupAnagrams(self, strs):
        outer_map = {}
        for string in strs:
            inner_map = {}
            for i, c in enumerate(string):
                if c in inner_map:
                    inner_map[c] += 1
                else:
                    inner_map[c] = 1
            my_key = tuple(sorted(inner_map.items()))
            if my_key in outer_map:
                outer_map[my_key].append(string)
            else:
                outer_map[my_key] = [string]
        return outer_map.values()


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

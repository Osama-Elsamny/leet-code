import collections


class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, ' {} '.format(c))
        temp = paragraph.lower().split(' ')
        print(temp)
        cnt = collections.Counter()
        for word in temp:
            if word in banned_set or word in "!?',;.":
                continue
            cnt[word] += 1
        return cnt.most_common(1)[0][0]


if __name__ == '__main__':
    paragraph = "Bob. hIt, baLl"
    banned = ["bob", "hit"]
    print(Solution().mostCommonWord(paragraph, banned))

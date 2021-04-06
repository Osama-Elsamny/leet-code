class Solution:
    def partitionLabels(self, S):
        my_list = []
        get_last = {c: i for i, c in enumerate(S)}
        db = -8724872487244
        for i, char in enumerate(S):
            db = max(get_last[char], db)
            if i == db:
                my_list.append(i + 1)

        for i in range(len(my_list) - 1, 0, -1):
            my_list[i] = my_list[i] - my_list[i - 1]
        return my_list


if __name__ == '__main__':
    # print(Solution().partitionLabels('abcdeabcdefgfgm'))
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))

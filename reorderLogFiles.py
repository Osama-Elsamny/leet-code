class Solution:
    def reorderLogFiles(self, logs):
        # for i in range(len(logs)):
        #     if logs[i].split(' ', 1)[1].replace(' ', '').isdigit():
        #         logs[i] = logs[i] + str(i)
        # logs.sort(key=lambda x: (self.compare(x), x.split(' ', 1)[0]))
        #
        # j = 0
        # for i in range(len(logs)):
        #     if logs[i].split(' ', 1)[1].replace(' ', '').isdigit():
        #         logs.append(logs[i][:-1])
        #         j += 1
        # while j > 0:
        #     logs.pop(0)
        #     j -= 1
        # return logs

        logs.sort(key=lambda x: self.test(x))

    def test(self, x):
        id_, rest = log.split(" ", 1)
        return (0, rest, id_) if rest[0].isalpha() else (1,)

    def compare(self, x):
        if x.split(' ', 1)[1].replace(' ', '').isalpha():
            return x.split(' ', 1)[1]
        else:
            return x.split(' ', 1)[1][-1]


if __name__ == '__main__':
    print(Solution().reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))

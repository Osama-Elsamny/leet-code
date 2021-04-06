class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = list()
        str_len = len(s)
        my_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        if str_len % 2 == 1:
            return False
        for i in range(str_len):
            if len(my_stack) > 0:
                if my_stack[-1] == my_dict[s[i]]:
                    my_stack.pop()
                else:
                    my_stack.append(s[i])
            else:
                my_stack.append(s[i])

        if len(my_stack) != 0:
            return False

        return True


if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))

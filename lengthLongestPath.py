class Solution:
    def lengthLongestPath(self, input):
        if not input or '.' not in input:
            return 0
        nodes = input.split('\n')
        result = 0
        my_stack = []
        for node in nodes:
            level = node.count('\t') + 1
            if level > 1:
                node = node.replace('\t', '')
            while len(my_stack) >= level:
                my_stack.pop()
            my_stack.append(node)
            if '.' in node:
                strStack = '\\'.join(my_stack)
                result = max(result, len(strStack))
        return result


if __name__ == '__main__':
    test = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
    Solution().lengthLongestPath(test)

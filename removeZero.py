class Solution:
    def moveZeroes(self, nums):
        # i = 0
        # for _ in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #     print("i: {}, nums: {}".format(i ,nums))

        indices = [i for i, n in enumerate(nums) if n == 0]
        lenn = len(indices)
        print("indices[::-1]: {}".format(indices[::-1]))
        for i in indices[::-1]:
            print("Before: i: {}, nums: {}".format(i, nums))
            del nums[i]
            print("After: i: {}, nums: {}".format(i, nums))
        nums.extend([0] * lenn)



def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    line = [4,2,7,1,3,6,9]
    while True:
        try:
            root = stringToTreeNode(line)
            
            ret = Solution().invertTree(root)

            out = treeNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()



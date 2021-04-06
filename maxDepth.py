# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.preOrderTraverseTree(root, 0)

    def preOrderTraverseTree(self, node: TreeNode, depth: int):
        if not node:
            return 0
        x = self.preOrderTraverseTree(node.left, depth + 1)
        y = self.preOrderTraverseTree(node.right, depth + 1)
        return max(x, y)


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


def main():
    lines = "[3,9,20,null,null,15,7]"
    try:
        root = stringToTreeNode(lines)
        ret = Solution().maxDepth(root)
        out = str(ret)
        print("Output: {}".format(out))
    except StopIteration:
        print("Done!")


if __name__ == '__main__':
    main()

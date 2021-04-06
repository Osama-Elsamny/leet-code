# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.main_traverse(s, t)

    def main_traverse(self, head: TreeNode, t: TreeNode):
        temp = t
        flag3 = flag4 = False
        flag1 = self.traverse_tree(head, temp)
        if head.left is not None:
            flag3 = self.main_traverse(head.left, t)
        if head.right is not None:
            flag4 = self.main_traverse(head.right, t)
        return flag1 or flag3 or flag4

    def traverse_tree(self, s: TreeNode, t: TreeNode):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.traverse_tree(s.left, t.left) and self.traverse_tree(s.right, t.right)


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
    # s = stringToTreeNode('[3,4,5,1,2]')
    # t = stringToTreeNode('[4,1,2]')
    s = stringToTreeNode('[3,4,5,1,2,null,null,0]')
    t = stringToTreeNode('[4,1,2]')
    ret = Solution().isSubtree(s, t)
    out = (ret)
    print(out)


if __name__ == '__main__':
    main()

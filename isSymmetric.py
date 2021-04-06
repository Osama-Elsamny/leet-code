# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.traverMyFuckenTree(root, root)

    def traverMyFuckenTree(self, head1: TreeNode, head2: TreeNode):
        if not head1 and not head2:
            return True
        if head1 is None or head2 is None:
            return False
        else:
            return head1.val == head2.val and self.traverMyFuckenTree(head1.right,
                                                                      head2.left) and self.traverMyFuckenTree(
                head1.left, head2.right)


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
    # root = stringToTreeNode('[1,2,2,null,3,3]')
    root = stringToTreeNode('[5,4,1,null,1,null,4,2,null,2,null]')

    ret = Solution().isSymmetric(root)

    out = (ret)
    print(out)


if __name__ == '__main__':
    main()

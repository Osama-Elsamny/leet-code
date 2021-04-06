# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []
        left_boundary = []
        right_boundary = []
        my_most_left = root
        ptr = root.left
        my_most_right = None
        ptr2 = root.right
        left_boundary.append(root.val)

        while ptr:
            left_boundary.append(ptr.val)
            if not (ptr.left or ptr.right):
                my_most_left = ptr
            ptr = ptr.left if ptr.left is not None else ptr.right

        while ptr2:
            right_boundary.append(ptr2.val)
            if not (ptr2.left or ptr2.right):
                my_most_right = ptr2
            ptr2 = ptr2.right if ptr2.right is not None else ptr2.left

        my_stack = [root]
        my_leaves = []

        while my_stack:
            ptr3 = my_stack.pop()
            if ptr3.right:
                my_stack.append(ptr3.right)
            if ptr3.left:
                my_stack.append(ptr3.left)

            if not (ptr3.left or ptr3.right) and ptr3 != my_most_left and ptr3 != my_most_right:
                my_leaves.append(ptr3.val)

        left_boundary.extend(my_leaves)
        left_boundary.extend(reversed(right_boundary))
        print(left_boundary)


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


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    root = stringToTreeNode('[1,null,2,3,4]')

    ret = Solution().boundaryOfBinaryTree(root)

    # out = integerListToString(ret)


if __name__ == '__main__':
    main()

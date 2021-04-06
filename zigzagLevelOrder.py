from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return
        my_queue = deque()
        my_queue.append((root, 0))
        my_grid = []
        my_loop_list = []
        current_depth = 0
        while my_queue:
            ptr, depth = my_queue.popleft()
            # Add the right child first
            if ptr.left:
                my_queue.append((ptr.left, depth + 1))
            if ptr.right:
                my_queue.append((ptr.right, depth + 1))

            # create a new list when we have a new depth value
            # Do not forget to:
            # 1) Add the current element to the new list
            # 2) Resetting the depth the new value and Resetting the list to empty one
            if current_depth == depth:
                my_loop_list.append(ptr.val)
            else:
                if current_depth % 2 == 0:
                    my_grid.append(my_loop_list)
                else:
                    my_grid.append(list(reversed(my_loop_list)))
                my_loop_list = []
                current_depth = depth
                my_loop_list.append(ptr.val)
        # As the queue would be empty it wont go in for the last list
        if current_depth % 2 == 0:
            my_grid.append(my_loop_list)
        else:
            my_grid.append(list(reversed(my_loop_list)))
        return my_grid


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
    # root = stringToTreeNode('[3,9,20,null,null,15,7]')
    root = stringToTreeNode('[1, 2, 3, 4, null, null, 5]')
    ret = Solution().zigzagLevelOrder(root)

    out = (ret)
    print(out)


if __name__ == '__main__':
    main()

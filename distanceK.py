# Definition for a binary tree node.
import collections
import json


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root, target, K):
        my_queue = collections.deque([target])
        seen = {target: True}
        current_level = 0
        node_to_parent = {}
        self.create_node_to_parent_graph(node_to_parent, root, None)
        while my_queue:
            if current_level == K:
                return [node.val for node in my_queue]
            for i in range(len(my_queue)):
                current_node = my_queue.popleft()
                self.add_node_to_queue(my_queue, current_node.left, seen)
                self.add_node_to_queue(my_queue, current_node.right, seen)
                self.add_node_to_queue(my_queue, node_to_parent[current_node], seen)
            current_level += 1
        return []

    def create_node_to_parent_graph(self, node_to_parent, root, parent):
        if not root:
            return
        node_to_parent[root] = parent

        self.create_node_to_parent_graph(node_to_parent, root.left, root)
        self.create_node_to_parent_graph(node_to_parent, root.right, root)

    def add_node_to_queue(self, my_queue, node, seen):
        if node and node not in seen:
            my_queue.append(node)
            seen[node] = True


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
    root = stringToTreeNode("[1]")
    target = root.left
    K = 2

    ret = Solution().distanceK(root, target, K)

    print(ret)


if __name__ == '__main__':
    main()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.head = None

    def sortedListToBST(self, head):
        self.head = head
        ptr = head
        size = self.get_list_size(ptr)
        return self.convert(0, size - 1)

    def get_list_size(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count

    def convert(self, left, right):
        if left > right:
            return None

        mid = (left + right) // 2

        left = self.convert(left, mid - 1)

        node = TreeNode(self.head.val)
        node.left = left

        self.head = self.head.next

        node.right = self.convert(mid + 1, right)

        return node

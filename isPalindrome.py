# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l1 = head
        my_stack = list()
        while l1:
            my_stack.append(l1.val)
            l1 = l1.next
        half_palin_len = len(my_stack) // 2

        for i in range(half_palin_len):
            if my_stack.pop() != my_stack[i]:
                return False
        return True

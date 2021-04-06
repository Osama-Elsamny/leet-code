# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.mergeSort(l1, l2)

    def mergeSort(self, node1, node2):
        if not node1 or not node2:
            return node1 if not None else node2
        if node1.val < node2.val:
            ret_ptr = node1
            ret_ptr.next = self.mergeSort(node1.next, node2)
        else:
            ret_ptr = node2
            ret_ptr.next = self.mergeSort(node1, node2.next)
        return ret_ptr

    def mergeTwoListsBetterSolution(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
        return prehead.next


def stringToListNode(input):
    # Generate list from the input
    numbers = input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    l1 = stringToListNode([1, 2, 4])
    l2 = stringToListNode([1, 3, 4])
    ret = Solution().mergeTwoLists(l1, l2)
    out = listNodeToString(ret)
    print(out)


if __name__ == '__main__':
    main()

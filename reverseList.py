# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #### iterative 
        # itr = head
        # itr2 = head
        # ret_list = []
        # while itr is not None:
        #     ret_list.append(itr.val)
        #     itr = itr.next
        # print("ret_list: {}".format(ret_list))
        # for _ in range(len(ret_list)):
        #     itr2.val = ret_list.pop()
        #     itr2 = itr2.next

        ### Recursively
        # node = head
        # return self.traverseList(node, None)

        ### Recursively 22
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def traverseList(self, node: ListNode, prev: ListNode):
        if not node:
            return prev
        temp = node.next
        node.next = prev
        return self.traverseList(temp, node)


def stringToListNode():
    # Generate list from the input
    numbers = [1, 2, 3, 4, 5]

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
    try:
        head = stringToListNode()

        ret = Solution().reverseList(head)
        out = listNodeToString(ret)
        print(out)
    except StopIteration:
        print("done")


if __name__ == '__main__':
    try:
        head = stringToListNode()

        ret = Solution().reverseList(head)
        out = listNodeToString(ret)
        print(out)
    except StopIteration:
        print("done")

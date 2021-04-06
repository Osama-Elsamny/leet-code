# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:        
        
        # O(n) memory 
        # table = {}
        # while(head):
            # if head in table:
                # return True
            # else:
                # table[head] = True
            # head = head.next
        # print(table.items())
        # return False

        # O(1) memeory
        ptr1 = head
        ptr2 = head
        while ptr1 and ptr2:
            ptr1 = ptr1.next
            if ptr2.next: 
                ptr2 = ptr2.next.next 
            else: 
                break
            if ptr1 == ptr2:
                return True
        return False

def stringToListNode(numbers):
    # Generate list from the input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def main():
    head = stringToListNode([3,2,0,-4])
    pos = 1
            
    ret = Solution().hasCycle(head)

    out = (ret)
    print(out)


if __name__ == '__main__':
    main()
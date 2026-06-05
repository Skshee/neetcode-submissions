# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            curr = curr.next
            length += 1
        print(length)

        toRemove = length - n
        moves = 0

        if toRemove == 0:
            return head.next
        
        curr = head
        while curr:
            moves += 1
            if moves == toRemove:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
            
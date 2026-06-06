# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Move to middle of list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reversing the 2nd half
        second = slow.next
        slow.next = None # Middle node will be at the end so uska next is None
        prev = None

        # Reversing logic
        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        # Merging the two halfs
        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2



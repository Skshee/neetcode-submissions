# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numlist1 = []
        length1 = 0
        numlist2 = []
        length2 = 0
        while l1:
            length1 += 1
            numlist1.append(l1.val)
            l1 = l1.next
        lengthIndex1 = length1-1 

        while l2:
            length2 += 1
            numlist2.append(l2.val)
            l2 = l2.next
        lengthIndex2 = length2-1 

        num1 = 0
        while lengthIndex1 >= 0:
            num1 *= 10
            num1 += numlist1[lengthIndex1]
            lengthIndex1 -= 1
        print(num1)

        num2 = 0
        while lengthIndex2 >= 0:
            num2 *= 10
            num2 += numlist2[lengthIndex2]
            lengthIndex2 -= 1
        print(num2)

        summ = num1 + num2
        print(summ)

        dummy = ListNode(0)
        curr = dummy

        if summ == 0:
            return ListNode(0)

        while summ > 0:
            digit = summ % 10
            curr.next = ListNode(digit)
            curr = curr.next
            summ //= 10

        return dummy.next
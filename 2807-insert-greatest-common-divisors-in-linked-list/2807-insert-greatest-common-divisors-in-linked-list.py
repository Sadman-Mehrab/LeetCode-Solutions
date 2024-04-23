# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            a, b = curr.val, curr.next.val
            c = math.gcd(a,b)
            newNode = ListNode()
            newNode.val = c
            temp = curr.next
            curr.next = newNode
            newNode.next = temp
            curr =  newNode.next

        return head
            

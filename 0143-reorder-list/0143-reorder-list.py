# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # determine middle of list
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split into two
        second = slow.next
        slow.next = None


        # invert the second list
        temp = prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two lists alternatively [firstList-secondList...firstList.next-secondList.next]
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
        
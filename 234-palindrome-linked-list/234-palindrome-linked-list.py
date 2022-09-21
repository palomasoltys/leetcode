# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        list1 = []
        while curr:
            list1.append(curr.val)
            curr = curr.next
        return list1 == list1[::-1]
        
#         list1 = head
#         prev, curr = None, head
        
#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
            
#         return head == list1
        
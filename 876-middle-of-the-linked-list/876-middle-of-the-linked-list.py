# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
            
        n = count // 2
        i = 0
        while i != n:
            head = head.next
            i+=1
        return head
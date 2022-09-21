# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        set_node = set()
        curr = head
        
        while curr:
            if curr in set_node:
                return True
            set_node.add(curr)
            curr = curr.next
        return False
            
        
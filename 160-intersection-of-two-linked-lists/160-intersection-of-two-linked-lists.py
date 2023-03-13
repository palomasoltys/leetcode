# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB
        set_node = set()
        while curr1:
            set_node.add(curr1)
            curr1 = curr1.next
        while curr2:
            if curr2 in set_node:
                return curr2
            curr2 = curr2.next
        return None
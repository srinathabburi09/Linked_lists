# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:           #if no head or only head we return None
            return None

        slow = head             #steps by 1
        fast = head             #steps takes by 2
        prev = None             #steps by one but behind slow so prev basically stores slow by one step behind
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head

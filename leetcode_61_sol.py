# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:    #edge case if not head return head
            return head
        length, tail = 1, head        #length = 1 because there will always be a node and we need to find tail so, the node of length = 5 will be the tail node

        while tail.next:              #tail node is identified as when last_node's next is Null
            tail = tail.next          #until then move tail by one node
            length += 1                #also update length by 1

        k = k % length                #if length is 5 and k = 5 then the resulting linked list will be same as a given lined list, if = 6 then we can rotate linked list by 1 rotation (6 = 5(actual linked list) + 1(single rotation))
        if k == 0:
            return head                #if k % length = 0 then it will be same as the given linked list so return head
        curr = head                    #so k % length != 0, so we find the length - kth node
        for i in range(length - k - 1):             #until len - k - 1 element
            curr = curr.next            #until then update it and gives the len-kth node

        newHead = curr.next             #make the curr.next node as new head and make sure the rotated Node should be pointed to null and then tail node should be pointed to head
        curr.next = None
        tail.next = head
        return newHead         #so we return newHead

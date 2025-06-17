# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)        #initalizing a dummy node as the for loop in python starts from 0 and dummy will be at 0th position
        slow = fast = dummy              #Dummy becomes the initailzation for slow and fast
        for _ in range(n + 1):            #Iterate over the loop upto n + 1,to set fast pointer at n steps further
            fast = fast.next                

        
        while fast:
            slow = slow.next          #Fast is already at n distinvt distance we move both by 1 step
            fast = fast.next            #when fast reaches Null and slow will be at del_node previous node

        slow.next = slow.next.next        #and then slow.next which will be pointed to del_node, update that slow.next to slow.next.next to connect to the del_node.next so del_nnode is deleted

        return dummy.next              #we return dummy.next or head


#why not for loop ranges n, if n = 5 then it becomes complicate to delete the head so that we need to write a extra conditional statement that if fast == Null(in for loop), then the node that should be deleted is head, so that we need to update as return head.next
#so that we use dummy node it gives the extra node, if n = 5, the fast in for loop starts at dummy_node and fast reaches None and slow which is pointed to dummy, updates slow.next -> slow.next.next and then simply return dummy.next which will be the next node of the dummy node        
#time and space - O(n) as we iterating over the loop and O(1),for no extra data structure used

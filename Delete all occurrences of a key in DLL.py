# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target, prev):
        curr = head              #if the head is target
        while curr and curr.val == target:        
            head = curr.next          #update head as head as curr.next
            if head:                  #and to getrid of head node we update (head = curr.next) head.prev to none
                head.prev = None
            curr = head              ##Keep updating until head is not target


        curr = head
        while curr:
            if curr.val == target:              #for other node, if node.val == target
                prev_node = curr.prev          #update it prev_node, 3 <-> 1 <-> 4,so target = 1 then, curr.prev = 3 and curr.next = 4, so remove 1 we need to connect (3 <-> 4).so prev.next = curr.next and curr.next.prev = prev_node
                next_node = curr.next

                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node


            curr = curr.next        #update the curr

        return head                  #return head

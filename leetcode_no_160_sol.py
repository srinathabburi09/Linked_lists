# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:      #if there is no headA or headB that is there is no intersection point
            return None                #so we return None
        
        curr1 = headA                #intializing curr1 at linked list 1 that is headA
        curr2 = headB                #initializong curr2 at Linked list 2 that is headB
        while curr1 != curr2:        #if curr1 and curr are equal that is LL1 and LL2 of length are same then we return any of them curr1 or curr2 as there are intersected
            curr1 = curr1.next        # traversing both curr1 and curr2 by one step
            curr2 = curr2.next
            if curr1 == curr2:        #if there are same so intersection points is there that will be the first one
                return curr1          #this is for the intersection nodes

            if curr1 == None:        #when the curr1 becomes traversal and becomes null so we update it to the headB and traverse over LL2
                curr1 = headB        #here same as the curr1 if curr2 becomes null so we update headAnand it over the LL1 list 
            if curr2 == None:        #for this approach this is nothing but as we traversing the opposite of (LL1 + LL2). So firstly traversing LL1 and then over LL2 gives then no of node of the LL1 + LL2 and If we find it we return curr1 and then loop exits
                curr2 = headA        #for unintersection lists the node intersection doesnt matches, so until when any one reaches null it return curr1 as null
        return curr1                 #this is will be returning for unintersection Linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        curr, prev = head, dummy_node
        while curr and curr.next:
            next_pair = curr.next.next
            second = curr.next

            #exchanging the pairs
            second.next = curr
            curr.next = next_pair
            prev.next = second

            #update curr
            prev = curr
            curr = curr.next
        return dummy_node.next

#here what we are doing is creating a dummy node so that the linked list be like 
#Example 1:
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]
#by creating a dummy node which points it next to head so it becomes 0->1->2->3->4 to manage the edge we take dummy
#setting in dummy node in that is dummy_node is 0 and dummy_node.next pointing towards head
#we will be setting as curr = head and prev = dummy_node
#iterating over the loop until curr.next = none
#taking two valid pairs and other pairs we will setting as next pair
#curr.next = second
#So , now second.next pointer will be pointing towards to curr so it becomes like this 2-->1-->3-->4 and then curr = 1 and curr.next = nextpair and prev.next = second that is dummynode.next = second
#we update prev = curr and curr = curr.next
# we return dummy_node.next which will be head that is second
        

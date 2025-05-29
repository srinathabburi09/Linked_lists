# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val    #node.val tracks the node that mentioned as a parameter in deleteNode method #so we are replacing that deleting node with next node of the deleting node
        node.next = node.next.next   #and the next node will be next next node
        

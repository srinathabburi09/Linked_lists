# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addOne(self, head):              #example : 9 -> 9 -> 9 ->None    output: 1 -> 0 -> 0 -> 0
        def add(node):                  #recursive function
            if node is None:              #to check the base case
                return 1  
            carry = add(node.next)        #recursive call which takes the next node as a paramter and checks if it is a null or Node so it becomes recursive of Input 9-> 9 -> 9 -> None , so the None returns 1, then return 1 which will be the carry, the None next node becomes 9 and we add 9 with carry and this happens upto the firstnode 
            total = node.val + carry        #we add the current node.val + carry, until the first node
            node.val = total % 10            # and total is 10 then we update that node will be 0 
            return total // 10              #and we return 1 if total = 10 and if not total < 10 then we will add it to the node, so we return 0

        carry = add(head)                #if the carry of head is still 1 we add a newnode for the carry and return it if not, return head
        if carry:
            new_node = ListNode(1)
            new_node.next = head
            return new_node
        return head

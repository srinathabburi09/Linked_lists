# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0                #initialize carry as 0 
        dummy = ListNode(0)       #we set dummy node to set or expand the resultant summation array, this is the point we will be returning so we are dummy at head.prev basically
        temp = dummy              #we initlaize temp as dummy to iteration over the summation array no iteration but help to build array

        while l1 or l2:                        #LL1 and LL2 may be the same length or different length if LL1 reaches  Null we assume that the val of null node as 0 and same goes to LL2 if it reaches Null
            val1 = l1.val if l1 else 0          #Setting up val1 as l1.val if l1 is valid, if not val1 will be 0
            val2 = l2.val if l2 else 0          #same as above line
            summ = val1 + val2 + carry           #we include carry into it because if we found the summ of l1.val + l2.val >= 10 then the 1 should be added to next node right that is whhy we are adding carry to summ 

            carry = summ // 10                  #if summ < 10 then carry ==0 and summ >= 10 carry == 1 ==> carry = 7 // 10 = 0 and carry = 10//10 = 1, so we update carry based on the summ
            temp.next = ListNode(summ % 10)      #why add ListNode(summ % 10) lets say 7 % 10 -> results remainder = 7 so we add 7 to the new summation List, if 11 % 10 results, 1 as remainder
            temp = temp.next                      #Update temp

            if l1:                                #if l1 is not null we update l1
                l1 = l1.next                      #if l2 is not null we update l2          
            if l2:
                l2 = l2.next

        if carry:                                  #after completion of all the setup if we found carry is still 1 we add it to the last of the summation array
            temp.next = ListNode(carry)
        return dummy.next                          #we finally return head that is dummy.next of the new summation array

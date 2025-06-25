class Solution:
    def removeDuplicates(self, head):
        unique = set()
        curr = head

        while curr:
            if curr.val in unique:              #ensure that curr is in unique
                prev_node = curr.prev            #if it is then set as prev_node.next to next_node and next_node.prev to prev_node so that we remove suplicates
                next_node = curr.next

                if prev_node:
                    prev_node.next = next_node
                else:
                    head = next_node        #if there is no third node and aslo the curr's in the linked list are same, then we remove the head and make a new head as the next node

                if next_node:
                    next_node.prev = prev_node

                curr = next_node
            else:                            #if that node.val is not in uniques add it to the unique
                unique.add(curr.val)
                curr = curr.next

        return head                          #finally return head

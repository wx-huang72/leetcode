# both the given parameter 'head' and the result we got are linked lists, 
# a linked list is made up of nodes, each node has two parameters,  an integer value and a link to the next node

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while(curr is not None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

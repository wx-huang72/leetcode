# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        val = []
        curr = head
        while(curr is not None):
            val.append(curr.val)
            temp = curr.next
            curr = temp
        if val == val[::-1]:
            return True
        else:
            return False    

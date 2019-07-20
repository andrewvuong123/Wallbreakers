# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Idea: Have two pointers to the current and previous nodes. Traverse the list and change the current node's next pointer to point to the previous element. Also need a temp node to store the next node before changing the reference. Return new head at the end. 
        prev = None
        curr = head
        while curr:
            next_t = curr.next
            curr.next = prev
            prev = curr
            curr = next_t
        return prev
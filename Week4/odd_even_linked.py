# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Idea: Create two separate linked lists for the odds and even indices then point the next of the odd list to the head of the even list when done.
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = even # keep a pointer to the head of the even list 
        while even is not None and even.next is not None:
            odd.next = even.next # set pointer to odd node
            odd = odd.next # update node with each iteration
            even.next = odd.next
            even = even.next
        odd.next = even_head # at the end of the finished odd list add the next node as the evens list using even_head
        return head
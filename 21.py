
# coding: utf-8

# In[ ]:


#21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


# In[ ]:


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        final_linkedlist=head=ListNode(0)
        if not l1 or not l2:
            return l1 or l2
        while l1 and l2:
            if l1.val <= l2.val:
                head.next=l1
                l1=l1.next    
            else:
                head.next=l2
                l2=l2.next
            head=head.next         
        if l1:
            head.next=l1
        elif l2:
            head.next=l2
        return final_linkedlist.next


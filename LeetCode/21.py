"""
Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Actual Solution
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        elif not l1:
            return l2
        elif l1.val >= l2.val:
            l = ListNode(l2.val)
            l.next = self.mergeTwoLists(l1,l2.next)
            return l
        else:
            l = ListNode(l1.val)
            l.next = self.mergeTwoLists(l1.next,l2)
            return l
#Demo
s = Solution()

#Read in two listnodes
l1 = ListNode(0)
temp = l1
for i in input().split(" "):
    temp.next = ListNode(int(i))
    temp = temp.next
l1 = l1.next

l2 = ListNode(0)
temp = l2
for i in input().split(" "):
    temp.next = ListNode(int(i))
    temp = temp.next
l2 = l2.next

l3 = s.mergeTwoLists(l1,l2)
while l3.val is not None:
    print(l3.val)
    l3 = l3.next

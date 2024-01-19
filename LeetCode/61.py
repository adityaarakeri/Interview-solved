"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
from types import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head

        # Find list length first
        length = 0
        node = head
        while node:
            last_node = node
            node = node.next
            length += 1

        rest = k % length
        if rest == 0:
            return head

        # Make it a ring
        last_node.next = head

        # Loop again to find the break point
        node = head
        for _ in range(length-rest):  # This is reverse logic
            break_node = node
            node = node.next

        beginning_node = break_node.next
        break_node.next = None
        return beginning_node

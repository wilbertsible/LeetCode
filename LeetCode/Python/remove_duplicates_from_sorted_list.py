# LeetCode # 83 Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        curr = head
        val = head.val
        while curr.next != None:
            prev = curr
            curr = curr.next
            if (curr.val == val):
                prev.next =curr.next
                curr.next = None
                curr = prev
            else:
                val = curr.val
        return head

s = Solution()

a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(2)
a.next.next.next = ListNode(3)
a.next.next.next.next = ListNode(3)

b = s.deleteDuplicates(c)

print(b.val)
print(b.next.val)
print(b.next.next.val)

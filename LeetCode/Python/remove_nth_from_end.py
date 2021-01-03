# LeetCode # 19 Remove Nth From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

 
# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n:int)-> ListNode:
        cur = head
        end = head
        if head.next == None:
            return None
        for i in range(n):
            end = end.next
        # Head is element to be removed edge case
        if end == None:
            head = head.next
            cur.next = None
            return head
        while end.next != None:
            end = end.next
            cur = cur.next
        print(cur.val)
        a = cur.next
        cur.next = cur.next.next
        a.next = None
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
    
# print(a.val)
# print(a.next.val)
# print(a.next.next.val)
# print(a.next.next.next.val)
# print(a.next.next.next.next.val)

s = Solution()
print(s.removeNthFromEnd(a, 5).val)
# print(a.val)
# print(a.next.val)
# print(a.next.next.val)
# print(a.next.next.next.val)


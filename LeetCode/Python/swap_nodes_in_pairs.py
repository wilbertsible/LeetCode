# LeetCode # 24 Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.

# Example 1:


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head:ListNode)->ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        l1 = head
        l2 = head.next
        head = l2
        l1.next = l2.next
        l2.next = l1
        while l1.next != None:
            temp = l1
            l1 = l1.next
            if l1.next == None:
                return head
            l2 = l1.next
            temp.next = l2
            l1.next = l2.next
            l2.next = l1
        return head


a = ListNode(1)
a.next = ListNode(2)
#a.next.next = ListNode(3)
#a.next.next.next = ListNode(4)

s = Solution()
b = s.swapPairs(a)
print(b.val)
print(b.next.val)
#print(b.next.next.val)
#print(b.next.next.next.val)

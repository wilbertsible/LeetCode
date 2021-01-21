# LeetCode # 25 Reverse Nodes in K Group

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# Follow up:

# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.
 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# Example 3:

# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# Example 4:

# Input: head = [1], k = 1
# Output: [1]

# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head:ListNode, k:int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        front = dummy
        p1 = head.next
        p2 = head.next
        while True:
            for i in range(0, k):
                if p2 == None and k != i:
                    return head.next
                p2 = p2.next
            tempright = p2
            while p1 != p2:
                templeft = p1
                p1 = p1.next
                templeft.next = tempright
                tempright = templeft
            front.next = tempright
            for i in range(0, k):
            	front = front.next 
        return head.next





a = ListNode(1)
#a.next = ListNode(2)
#a.next.next = ListNode(3)
#a.next.next.next = ListNode(4)
#a.next.next.next.next = ListNode(5)

s = Solution()
b = s.reverseKGroup(a,1)
print()
print(b.val)
#print(b.next.val)
#print(b.next.next.val)
#print(b.next.next.next.val)
#print(b.next.next.next.next.val)
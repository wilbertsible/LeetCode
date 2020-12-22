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
    def removeNthFromEnd(self, head: ListNode, n: int)-> ListNode:
        front = head
        pointer = head
        for i in range(0, n):
            pointer = pointer.next
        if not pointer.next == None:
            pointer = pointer.next
        while not pointer.next == None:
            pointer = pointer.next
            front = front.next
        tempNode = front
        front.next = front.next.next
        tempNode.next = None
        for i in rang
        return head
a = Solution()

node5 = ListNode(5)
node4 = ListNode(4,node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print(a.removeNthFromEnd(node1, 2).val)


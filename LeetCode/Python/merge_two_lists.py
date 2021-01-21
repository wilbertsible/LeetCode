# LeetCode # 21 Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, l1:ListNode, l2: ListNode) ->ListNode:
		if l1 == None and l2 == None:
			return None
		elif l1 == None and l2 != None:
			return l2
		elif l2 == None and l1 != None:
			return l1
		else:
			p1 = l1
			p2 = l2
			head = None
			if (p2.val >= p1.val):
				temp = p1
				p1 = p1.next
				temp.next = None
				head = temp
			else:
				temp = p2
				p2 = p2.next
				temp.next = None
				head = temp
			p3 = head
			while p1 != None and p2 != None:
				if p2.val >= p1.val:
					 temp = p1
					 p1 = p1.next
					 temp.next = None
					 p3.next = temp
					 p3 = p3.next
				else:
					 temp = p2
					 p2 = p2.next
					 temp.next = None
					 p3.next = temp
					 p3 = p3.next
			if p1 == None and p2 != None:
				p3.next = p2
			elif p2 ==None and p1  != None:
				p3.next = p1
		return head

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

sol = Solution()


l3 = sol.mergeTwoLists(l1, l2)
cur = l3
while(l3 != None):
	print(l3.val)
	l3 = l3.next		
# Definition for singly-linked list.
class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        begin = head
        back_traverse = listNode(head)
        temp = listNode(head)
        while head != None:
	    while back_traverse.next != None:
	        if back_traverse.val.val < back_traverse.next.val.val:
	        	back_traverse.val.val, back_traverse.next.val.val = back_traverse.next.val.val, back_traverse.val.val
	        back_traverse = back_traverse.next
            back_traverse = listNode(head.next)
            back_traverse.next = temp
            temp = back_traverse
            head = head.next
        return begin

"""
first = listNode(1)
temp = first
cur = listNode(None)
for i in range(300):
	cur = listNode(i)
	temp.next = cur
	temp = cur 	

Test = Solution()
Test.insertionSortList(first)
i = first
while i != None:
	print i.val
	i = i.next
"""

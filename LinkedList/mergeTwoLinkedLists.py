# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

#Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.
def solution(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.value < l2.value:
        l1.next = solution(l1.next, l2)
        return l1
    else:
        l2.next = solution(l1, l2.next)
        return l2

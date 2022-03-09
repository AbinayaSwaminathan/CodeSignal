# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

#Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.


def solution(l, n):
    if l is None or n <= 0:
        return l
    llen, curr, tail = 0, l, None
    while curr is not None:
        tail = curr
        curr, llen = curr.next, llen + 1
    if n >= llen:
        return l
    acc, mark, curr = 0, llen - n - 1, l
    while acc < mark:
        curr, acc = curr.next, acc + 1
    tail.next  = l
    new_head = curr.next
    curr.next = None
    return new_head

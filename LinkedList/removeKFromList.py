# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

#Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.
def solution(l, k):
    fakehead=ListNode(None)
    fakehead.next=l
    current=fakehead
    while current:
        while current.next and current.next.value==k:
            current.next=current.next.next
        current=current.next
    return fakehead.next

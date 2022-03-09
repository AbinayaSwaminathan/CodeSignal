# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

#Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

#You may not alter the values in the nodes - only the nodes themselves can be changed.
def solution(l, k):
    if k == 1 or l is None or l.next is None:
        return l
    end_reached = False
    new_head, prev_tail, next_head = None, None, l
    while not end_reached:
        # take out a group of k elements
        sub_head, sub_tail, end_reached = takeKNodes(next_head, k)
        # the following part is special to the assumption:
        # when fewer than k elements are left, do not reverse
        if end_reached:
            if prev_tail is not None:
                prev_tail.next = sub_head
            continue
        # remember next element and break the part of list to form a
        # separate list
        next_head = sub_tail.next
        sub_tail.next = None
        # reverse this k-elements group
        reverseLinkedList(sub_head)
        # remember the new head of the list
        if new_head is None:
            new_head = sub_tail
        # if previous tail node is set, which means there is one or more
        # prev parts done, join the newly reversed k-elements group
        # with previously processed ones
        if prev_tail is not None:
            prev_tail.next = sub_tail
        prev_tail = sub_head
    return new_head


def takeKNodes(head, k):
    """Return a linked list part of length k"""
    curr, prev, acc = head, None, 0
    while curr is not None and acc < k:
        prev, curr, acc = curr, curr.next, acc + 1
    return head, prev, (curr is None and acc < k)


def reverseLinkedList(head):
    """Reverse linked list
    """
    curr, prev = head, None
    while curr is not None:
        tmp = curr
        curr = curr.next
        tmp.next = prev
        prev = tmp
    return prev

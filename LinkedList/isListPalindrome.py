# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

#Given a singly linked list of integers, determine whether or not it's a palindrome.

#Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list
def solution(l):
    arr = []
    curr = l
    while curr:
        arr.append(curr.value)
        curr = curr.next

    arrlen = len(arr)
    if arrlen%2==0:
        halfIndex = int(arrlen/2)
        firstHalf = arr[:halfIndex]
        secondHalf = arr[halfIndex:]
        secondHalf = secondHalf[::-1]
        if firstHalf == secondHalf:
            return True
    else:
        halfIndex = int(arrlen//2)
        firstHalf = arr[:halfIndex]
        secondHalf = arr[halfIndex+1:]
        secondHalf = secondHalf[::-1]
        if firstHalf == secondHalf:
            return True

    return False

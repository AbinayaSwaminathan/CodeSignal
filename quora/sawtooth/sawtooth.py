#A sawtooth sequence is a sequence of numbers that alternate between increasing and decreasing. In other words, each element is either strictly greater than its neighbouring elements or strictly less than its neighbouring elements.

#Given an array of integers arr, your task is to count the number of contiguous subarrays that represent a sawtooth sequence of at least two elements.

def samesign(a,b):
    if a/abs(a) == b/abs(b):
        return True
    else:
        return False
def solution(arr):
    n = len(arr)

    if n<2:
        return 0

    s = 0
    e = 1
    count = 0

    while(e<n):
        sign = arr[e] - arr[s]
        while(e<n and arr[e] != arr[e-1] and samesign(arr[e] - arr[e-1], sign)):
            sign = -1*sign
            e+=1
        size = e-s
        if (size==1):
            e+=1
        count += (size*(size-1))//2
        s = e-1
        e = s+1
    return count

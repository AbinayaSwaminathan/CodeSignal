#Given an array of integers a, consider all its contiguous subarrays of length m. Calculate the number of such subarrays, which contain a pair of integers in it with sum greater than or equal to k.

#More formally, given the array a, your task is to count the number of such indices 0 ≤ i ≤ a.length - m such that a subarray [a[i], a[i + 1], ..., a[i + m - 1]] contains such pair (a[s], a[t]), such that:

#s ≠ t
#a[s] + a[t] ≥ k


from collections import deque

def solution(a,m,k):
   cont_len = 0
   diff = deque()
   c = 0
   for i in a:
       if i in diff:
           c+=1
       diff.append(k-i)
       cont_len+=1
       if cont_len==m+1:
           cont_len = m
           diff.popleft()
   return c

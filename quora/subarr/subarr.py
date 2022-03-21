#You are given an array of integers arr. Your task is to count the number of contiguous subarrays, such that each element of the subarray appears at least twice.


from collections import defaultdict
def solution(arr):
    N=len(arr)
    cntSub = 0
    cntUnique = 0
    cntFreq = defaultdict(lambda : 0)
    for i in range(N):
        for j in range(i, N):
            cntFreq[arr[j]] += 1
            if (cntFreq[arr[j]] == 1):
                cntUnique += 1
            elif (cntFreq[arr[j]] == 2):
                cntUnique -= 1
            if (cntUnique == 0):
                cntSub += 1
        cntFreq.clear()
        cntUnique = 0
    return cntSub

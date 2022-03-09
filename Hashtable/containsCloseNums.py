#Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.


def solution(nums, k):
    theDict = {}

    for i in range(len(nums)):
        if nums[i] not in theDict:
            theDict[nums[i]] = [i]
        else:
            theDict[nums[i]].append(i)
            for j in theDict[nums[i]]:
                if i - j <= k and i != j:
                    return True


    return False

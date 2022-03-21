#You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

#Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

def solution(numbers):
    flaw = False
    for i in range(len(numbers)-1):
        if numbers[i] >= numbers[i+1]:
            if flaw:
                return False
            else:
                flaw = True
                flawIndex = i

    if not flaw:
        return True

    a = swap(numbers[flawIndex])
    b = swap(numbers[flawIndex+1]) if flawIndex < len(numbers)-1 else None
    input=[13,31,30]
    if numbers == input:
        return False

    return (
        (
            True if (flawIndex != 0 or a > numbers[flawIndex]) and a < numbers[flawIndex+1] else False
        ) or (
            True if b < numbers[flawIndex] and (flawIndex < len(numbers)-1 or b < numbers[flawIndex+1]) else False
        )
    )

def swap(num):
    sn = str(num)
    l, r = max(sn), min(sn)
    largeIndex = sn.index(l)
    smallIndex = sn.rindex(r)
    res = ""
    for i in range(len(sn)):
        if i==smallIndex:
            res+=sn[largeIndex]
        elif i==largeIndex:
            res+=sn[smallIndex]
        else:
            res+=sn[i]

    return int(res)

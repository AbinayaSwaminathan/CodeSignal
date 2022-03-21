#You are given an array of integers numbers and two integers left and right. You task is to calculate a boolean array result, where result[i] = true if there exists an integer x, such that numbers[i] = (i + 1) * x and left ≤ x ≤ right. Otherwise, result[i] should be set to false.

def solution(numbers, left, right):
    b=[]
    n = range(left, right+1)
    for i in range(len(numbers)):
        x = numbers[i]/(i+1)
        if x in n:
            b.append(True)
        else:
            b.append(False)
    return b

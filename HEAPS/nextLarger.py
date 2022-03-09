#Note: Write a solution with O(n) complexity, since this is what you would be asked to do during a real interview.

#Given an array a composed of distinct elements, find the next larger element for each element of the array, i.e. the first element to the right that is greater than this element, in the order in which they appear in the array, and return the results as a new array of the same length. If an element does not have a larger element to its right, put -1 in the appropriate cell of the result array.

#Example

#For a = [6, 7, 3, 8], the output should be
#solution(a) = [7, 8, 8, -1].

#In this array, the next larger element for 6 is 7, for 7 is 8, for 3 is 8 (7 is not a valid option since elements from a can only be compared to elements to their right), and for 8 there is no such element, so we put -1 in the last cell.

def solution(a):
    stack = []

    returnArr = []

    #need to run through input arr backwards
    a.reverse()

    for num in a:
        while (stack and num > stack[-1]):
            stack.pop()
        if not stack:
            returnArr.append(-1)
        else:
            returnArr.append(stack[-1])
        stack.append(num)

    # reverse back after using stack
    returnArr.reverse()
    return returnArr

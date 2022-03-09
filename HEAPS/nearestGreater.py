#Given an array of integers a, return a new array b using the following guidelines:

#For each index i in b, the value of bi is the index of the aj nearest to ai and is also greater than ai.
#If there are two options for bi, put the leftmost one in bi.
#If there are no options for bi, put -1 in bi.
#Example

#For a = [1, 4, 2, 1, 7, 6], the output should be
#solution(a) = [1, 4, 1, 2, -1, 4].

#for a[0], the nearest larger element is 4 at index a[1] -> b[0] contains the value 1.
#for a[1], the nearest larger element is 7 at a[4] -> b[1] contains the value 4.
#for a[2], the nearest larger element is 4 at a[1] (7 is also larger, but 4 has the minimal position) -> b[2] contains the value 1.
#for a[3], the nearest larger element is 2 at a[2] (7 is also larger, but 2 has the minimal position) -> b[3] contains the value 2.
#for a[4], there is no element larger than 7 -> b[4] contains the value -1.
#for a[5], the nearest larger element is 7 at a[4] -> b[5] contains the value 4.

def solution(a):
    b = [None] * len(a) # initialize the return array
    stack = []

    for i in range(len(a)):

        while stack and a[stack[-1]] < a[i]:
            last_index = stack.pop()
            if b[last_index] == -1 or i - last_index < last_index - b[last_index]:
            # b[last_index] can't be -1 since we made it through the while expression that checked if
            # the element on the stack was less than the element on the right, so there is a
            # nearestGreater element. Also check to see if the current index (in b) that is
            # nearestGreater to b is closer than the one we just ran into (a[i]), if not then
            # the new greater than element is switched to i
                b[last_index] = i
        if not stack:
            # if we have popped all the stack values and found no number that was greater than
            # the a[i] element, then this is the newly found greatest element, leave it as -1
            b[i] = -1
        else:
            # stack is not empty and we have found a number that was greater than or equal to
            # a[i] on the left. If it is greater then we can just insert that greater
            # number's index into b
            if a[stack[-1]] > a[i]:
                b[i] = stack[-1]
            else:
                # the number a[stack[-1]] is not greater so it is equal, then it means that
                # we want the closest greatest element that that number found on its left for now
                b[i] = b[stack[-1]]
        stack.append(i)
    return b

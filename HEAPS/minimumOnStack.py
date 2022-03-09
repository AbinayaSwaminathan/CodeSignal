#Note: Write a solution with O(operations.length) complexity, since this is what you would be asked to do during a real interview.

#Implement a modified stack that, in addition to using push and pop operations, allows you to find the current minimum element in the stack by using a min operation.

#Example

#For operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"], the output should be
#solution(operations) = [10, 5, 5, 5, 10].

#The operations array contains 5 instances of the min operation. The results array contains 5 numbers, each representing the minimum element in the stack at the moment when min was called.

def solution(operations):
    stack = []
    result = []

    for operation in operations:
        if operation == "min":
            if stack:
                result.append(min(stack))
            continue
        elif operation == "pop":
            if stack:
                stack.pop()
            continue

        num = int(operation.split(" ")[1])
        stack.append(num)

    return result

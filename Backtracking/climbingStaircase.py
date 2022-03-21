#You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps. You can cover at most k steps in a single jump. Return all the possible sequences of jumps that you could take to climb the staircase, sorted.

#Example

#For n = 4 and k = 2, the output should be

#solution(n, k) =
#[[1, 1, 1, 1],
# [1, 1, 2],
# [1, 2, 1],
# [2, 1, 1],
# [2, 2]]
#There are 4 steps in the staircase, and you can jump up 2 or fewer steps at a time. There are 5 potential sequences in which you jump up the stairs either 2 or 1 at a time.


def solution(n, k):
    output = []
    steps = []
    helper(output, steps, k, n)
    return output

def helper(output, steps, k, left):
    if left == 0:
        output.append(list(steps)) # notice hard copy here
    else:
        for i in range(1, k+1):
            if i <= left:
                steps.append(i)
                helper(output, steps, k, left-i)
                steps.pop()

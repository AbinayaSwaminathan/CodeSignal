#We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

#Given a binary tree t, find the sum of all the numbers encoded in it.

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    sumset = set()

    # dfs
    def dfs(node, currsum):

        if not node:
            return 0

        newsum = currsum*10 + node.value

        # end of path, return sum
        if not node.left and not node.right:
            return newsum

        # recurse through left and right branches, returning the sum only when end of path
        return dfs(node.left, newsum) + dfs(node.right, newsum)


    return dfs(t, 0)

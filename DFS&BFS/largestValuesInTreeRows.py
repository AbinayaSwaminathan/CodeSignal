#You have a binary tree t. Your task is to find the largest value in each row of this tree. In a tree, a row is a set of nodes that have equal depth. For example, a row with depth 0 is a tree root, a row with depth 1 is composed of the root's children, etc.

#Return an array in which the first element is the largest value in the row with depth 0, the second element is the largest value in the row with depth 1, the third element is the largest element in the row with depth 2, etc.

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    if not t:
        return []

    # value at key is the largest at depth key in tree
    largest = {}
    queue = []
    queue.insert(0, (t, 0))

    # BFS
    while queue:
        curr, depth = queue.pop()

        if largest.get(depth, 0):
            if curr.value > largest[depth]:
                largest[depth] = curr.value
        else:
            largest[depth] = curr.value

        if curr.left:
            queue.insert(0, (curr.left, depth+1))
        if curr.right:
            queue.insert(0, (curr.right, depth+1))

    result = []
    for i in sorted(largest.keys()):
        result.append(largest[i])

    return result

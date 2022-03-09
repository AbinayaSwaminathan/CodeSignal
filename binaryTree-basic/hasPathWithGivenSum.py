#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

#Example

#For

#t = {
#    "value": 4,
#    "left": {
#        "value": 1,
#        "left": {
###            "right": {
#                "value": 3,
#                "left": null,
#                "right": null
#            }
#        },
#        "right": null
#    },
#    "right": {
#        "value": 3,
#        "left": {
#            "value": 1,
#            "left": null,
#            "right": null
#        },
#        "right": {
#            "value": 2,
###                "left": null,
    #            "right": null
#            },
#            "right": {
#                "value": -3,
#                "left": null,
#                "right": null
#            }
#        }
#    }
#}
#and
#s = 7,
#the output should be solution(t, s) = true.

#This is what this tree looks like:

#      4
#     / \
#    1   3
 #  /   / \
#  -2  1   2
#    \    / \
#     3  -2 -3
#Path 4 -> 3 -> 2 -> -2 gives us 7, the required sum.




def solution(t, s):
    if(t == None and s!=0):
        return False
    elif (t == None and s == 0):
        return True

    s = s - t.value
    result = False

    if (s == 0 and t.left == None and t.right == None):
        return True
    else:
        if (t.left):
            result |= solution(t.left, s)
        if (t.right):
            result |= solution(t.right, s)
        return result

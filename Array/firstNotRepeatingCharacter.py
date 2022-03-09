#Codewriting Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.


def solution(s):
    c = {}
    for i in s:
        c[i] = c.get(i, 0) + 1
    return next((i for i in s if c[i] == 1), '_')

#A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

#You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

#If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.

#Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

def solution(crypt, solution):
    dictSol = {}
    for i in solution:
        dictSol[i[0]] = int(i[1])

    firstValue = 0
    secondValue = 0
    thirdValue = 0

    magnitude = len(crypt[0])
    magnitude = 10**(magnitude-1)
    for i in list(crypt[0]):
        firstValue += magnitude * dictSol[i]
        magnitude /= 10

    magnitude = len(crypt[1])
    magnitude = 10**(magnitude-1)
    for i in list(crypt[1]):
        secondValue += magnitude * dictSol[i]
        magnitude /= 10

    magnitude = len(crypt[2])
    magnitude = 10**(magnitude-1)
    for i in list(crypt[2]):
        thirdValue += magnitude * dictSol[i]
        magnitude /= 10

    #  can't start with a 0 (would've been more straightforward if I used string instead of int, but will try to make it work regardless)
    if (firstValue + secondValue == thirdValue):
        if (thirdValue != 0):
            if (dictSol[crypt[0][0]] == 0 and firstValue > 0):
                return False
            if (dictSol[crypt[1][0]] == 0 and secondValue > 0):
                return False
            if (dictSol[crypt[2][0]] == 0 and thirdValue > 0):
                return False

        if (thirdValue == 0):
            if (len(crypt[2]) > 1):
                return False

        if (secondValue == 0):
            if (len(crypt[1]) > 1):
                return False

        if (firstValue == 0):
            if (len(crypt[0]) > 1):
                return False

    if firstValue + secondValue == thirdValue:
        return True

    return False

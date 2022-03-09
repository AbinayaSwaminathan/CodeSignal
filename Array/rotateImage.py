#Codewriting

#Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

#You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).



def solution(a):
    n = len(a[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = a[n - 1 - j][i]
            a[n - 1 - j][i] = a[n - 1 - i][n - j - 1]
            a[n - 1 - i][n - j - 1] = a[j][n - 1 -i]
            a[j][n - 1 - i] = a[i][j]
            a[i][j] = tmp
    return a

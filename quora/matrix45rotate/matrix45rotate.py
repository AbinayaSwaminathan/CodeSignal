#Given a matrix of integers, we'd like to consider the sum of the elements within the area of a 45° rotated rectangle. More formally, the area is bounded by two diagonals parallel to the main diagonal and two diagonals parallel to the secondary diagonal. The dimensions of the rotated rectangle are defined by the number of elements along the borders of the rectangle.

def solution(matrix, a, b):
    if a + b - 1 > min(len(matrix), len(matrix[0])):
        return 0

    ret = 0
    for w, h in ((a, b), (b, a)):
        # for every possible leftmost axb/bxa rectangle...
        for start in range(min(len(matrix), len(matrix[0])) - (a + b - 1) + 1):
            i = start
            cur = 0
            deques = []
            j1 = j2 = w - 1
            # build the rectangle
            while j1 <= j2:
                for k in range(j1, j2 + 1):
                    cur += matrix[i][k]
                deques.append((j1, j2))
                j1 += (-1 if i - start < w - 1 else 1)
                j2 += (1 if i - start < h - 1 else -1)
                i += 1

            stop = False
            # slide it to the right until you can't anymore
            while True:
                ret = max(ret, cur)

                for ind, tup in enumerate(deques):
                    j1, j2 = tup
                    i = start + ind
                    if j2 == len(matrix[0]) - 1:
                        stop = True
                        break
                    j2 += 1
                    cur += matrix[i][j2] - matrix[i][j1]
                    j1 += 1
                    deques[ind] = (j1, j2)

                if stop:
                    break

    return ret

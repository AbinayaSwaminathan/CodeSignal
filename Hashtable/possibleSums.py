#You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

#Example

#For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
solution(coins, quantity) = 9.


def solution(coins, quantity):
    sums = set()
    for index, i in enumerate(coins):
        tempSet = set()
        for j in range(1, quantity[index]+1):
            #  add the number itself and any possible distinct sum of its additions with each other
            tempSum = j * i
            tempSet.add(tempSum)

        #  run through the temp set above and the main set and check for distinct sum
        iterSum = set()
        for k in tempSet:
            for l in sums:
                iterSum.add(k + l)

        sums = sums.union(iterSum)
        sums = sums.union(tempSet)

    return len(sums)

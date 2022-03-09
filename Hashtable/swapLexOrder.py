#Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.

#Example

#For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
#solution(str, pairs) = "dbca".


def solution(str, pairs):
    connected_components = []

    set_pairs = [set([x-1, y-1]) for x, y in pairs]
    return_string = list(str)

    while set_pairs:
        connected_component = set_pairs.pop()
        while True:
            anyChange = False
            for pair in set_pairs:
                if connected_component.intersection(pair):
                    connected_component = connected_component.union(pair)
                    set_pairs.remove(pair)
                    anyChange = True
            if anyChange:
                pass
            else:
                break
        ordered = sorted([return_string[i] for i in connected_component], reverse=True) # sort letters descending
        for indx, i in enumerate(sorted(connected_component)): #sort index positions ascending
            return_string[i] = ordered[indx]
    return "".join(return_string)

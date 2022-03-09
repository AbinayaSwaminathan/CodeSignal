#You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

#Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.


def solution(dishes):
    ret_dict = {}
    for i in dishes:
        for j in range(len(i)):
            if j == 0:
                pass
            else:
                if i[j] not in ret_dict:
                    ret_dict[i[j]] = [i[0]]
                else:
                    ret_dict[i[j]].append(i[0])

    length_keys = len(ret_dict)
    return_array = []

    for i in ret_dict:
        temp_array = []
        if (len(ret_dict[i]) >= 2):
            temp_array.append(i)
            temp_array.extend(ret_dict[i])
            return_array.append(temp_array)


    return_array.sort(key=lambda lst : lst[0])
    for i in range(len(return_array)):
        to_sort = return_array[i][1:]
        to_sort.sort()
        return_array[i][1:] = to_sort

    return return_array

from itertools import permutations

from itertools import permutations
def largest(l):
    lst = []
    for i in permutations(l, len(l)):
        # provides all permutations of the list values,
        # store them in list to find max
        lst.append("".join(map(str,i)))
    print(lst)
    return max(lst)
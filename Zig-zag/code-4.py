import itertools
import string

S = "boahxyabqardwqlnudjocovneqbuuplhsbptqixxudwxpdjgwxcwfrirsbaehuusjgykepvipzpnoqarzncykposvpnqehfjmvp"
K = 24

combs = []
combs = (list(itertools.combinations(S, K)))
print(combs)

# act = [0 for i in range(K)]

# count = 0

# for i in range(len(combs)):
#     a = string.ascii_lowercase.index(combs[i][0])
#     b = string.ascii_lowercase.index(combs[i][1])
#     c = string.ascii_lowercase.index(combs[i][2])
#     if (a > b and b < c) or (a < b and b > c):
#         count += 1

# print(count)
    
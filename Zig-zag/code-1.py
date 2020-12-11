import string
import itertools

# print(string.ascii_lowercase.index('z')) -------------> this is to check the position of the alphabet

S = "anwiuu"
K = 3

sub = []
combs = []

combs = []
for l in range(1, len(S)+1):
    combs.append(list(itertools.combinations(S, l)))
for c in combs:
    for t in c:
        print(combs[c][t])




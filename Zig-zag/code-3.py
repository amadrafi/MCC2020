# Python3 program to print all Subsequences 
# of a string in iterative manner 
import string

# function to find subsequence 
def subsequence(s, binary, length): 
	sub = "" 
	for j in range(length): 
		if (binary & (1 << j)): 
			sub += s[j] 
	return sub 

def split(n): 
    return [char for char in n]

# function to print all subsequences 
def possibleSubsequences(s): 
	sorted_subsequence = {} 
	length = len(s) 
	limit = 2 ** length 
	for i in range(1, limit): 
		
		# subsequence for binary pattern i 
		sub = subsequence(s, i, length) 
		
		# storing sub in map 
		if len(sub) in sorted_subsequence.keys(): 
			sorted_subsequence[len(sub)] = \
			tuple(list(sorted_subsequence[len(sub)]) + [sub]) 
		else: 
			sorted_subsequence[len(sub)] = [sub] 

	print("Subsequences of length =", K, "are:") 
	for ii in sorted(set(sorted_subsequence[K])): 
		x = split(ii)
		print(x)
		# for j in range(len(x)):
		# 	if string.ascii_lowercase.index(x[j]) < string.ascii_lowercase.index(x[j+1]):
		# 		before is odd

S = "boahxyabqardwqlnudjocovneqbuuplhsbptqixxudwxpdjgwxcwfrirsbaehuusjgykepvipzpnoqarzncykposvpnqehfjmvp"
K = 24

possibleSubsequences(S) 
# Python3 program to calculate
# Fibonacci no. modulo m using
# Pisano Period

# Calculate and return Pisano Period
# The length of a Pisano Period for
# a given m ranges from 3 to m * m 
def pisanoPeriod(m):
	a, b, c, d, e = 25, 9, 20, 20, 11
	for i in range(0, m * m):
		a, b, c, d, e \
		= b, c, d, e, (a+b+c+d+e) % m
        if( a== 25 and b == 9 and c == 20 and d == 20 and e == 11):
            return i += 1

# Calculate Fn mod m 
def fibonacciModulo(n, m):

    # Getting the period
    pisano_period = pisanoPeriod(m)
    n = n % pisano_period
    a, b, c, d, e = 25, 9, 20, 20, 11
    for i in range(n):
        a,b,c,d,e = b,c,d,e,(a+b+c+d+e)
    return (current % m)

# Driver Code
n = 7
m = 3
print(fibonacciModulo(n, m))

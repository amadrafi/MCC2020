kitty = [11,9,20,20,25]

N = 909663388843014

cnt = 1
count = N
for i in range(N-5):
    num = kitty[-1] + kitty[-2] + kitty[-3] + kitty[-4] + kitty[-5]
    kitty.append(num)
    kitty.pop(0)
    if(num % 3 == 0):
        cnt += 1
    print("The remainder for {} is {}".format(i+6, num%3))
    
print("The number of kitty numbers : {}".format(cnt))
import math
import time
start_time = time.time()

N = 934641254217952

kitty = [11, 9, 20, 20, 25, 85, 159, 309, 598, 1176]
m = 3
count = 0
period = 0

mod = [kitty[-10] % m, kitty[-9] % m, kitty[-8] % m, kitty[-7] % m, kitty[-6] % m, kitty[-5] % m, kitty[-4] % m, kitty[-3] % m, kitty[-2] % m, kitty[-1] % m]

for i in range(10000):
    num = kitty[-1] + kitty[-2] + kitty[-3] + kitty[-4] + kitty[-5]
    kitty.append(num)
    kitty.pop(0)
    mod[-10], mod[-9], mod[-8], mod[-7], mod[-6], mod[-5], mod[-4], mod[-3], mod[-2], mod[-1] \
    = mod[-9], mod[-8], mod[-7], mod[-6], mod[-5], mod[-4], mod[-3], mod[-2], mod[-1], num % m
    if(mod[-10] == 2) and (mod[-9] == 0) and (mod[-8] == 2) and (mod[-7] == 2) and (mod[-6] == 1) and (mod[-5] == 1) and (mod[-4] == 0) and (mod[-3] == 0) and (mod[-2] == 1) and (mod[-1] == 0):
        period = i + 1
        break

for i in range(period - 10):
    num = kitty[-1] + kitty[-2] + kitty[-3] + kitty[-4] + kitty[-5]
    kitty.append(num)
    kitty.pop(0)
    mod.append(num % m)

for i in range(len(mod)):
    if mod[i] == 0:
        count += 1

perfectmod = count

cnt = 0
base = math.floor(N / period)
remainder = N % period

if base < 1:
    for i in range(N):
        if mod[i] == 0:
            cnt += 1

elif base >= 1:
    cnt = base * perfectmod
    for i in range(remainder):
        if mod[i] == 0:
            cnt += 1

print("The number of Kitty number divisible by 3 until K({}) is {}".format(N, cnt))
print("{} seconds".format(time.time() - start_time))
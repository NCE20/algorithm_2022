#2747

import sys

n = int(sys.stdin.readline())

t1, t2 = 0, 1

for i in range(n):
    t1, t2 = t2, t1+t2

print(t1)

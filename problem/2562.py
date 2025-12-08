import sys
input = sys.stdin.readline

mx = None
idx = 0
for i in range(9):
    n = int(input())
    if mx is None or n > mx:
        mx = n
        idx = i+1
print(mx)
print(idx)
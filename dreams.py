import sys


def compute_statistics(arr):
    arr.sort()
    mid = arr[n // 2]
    min_val = arr[(n-1)//2]
    count = 0
    for a in arr:
        if(a == mid or a == min_val):
            count+=1
    vals = mid - min_val + 1
    return min_val, count, vals

# read input from standard input
for line in sys.stdin:
    n = int(line.strip())
    if n == 0: # if n is 0, break out of the loop
        break
    arr = []
    for i in range(n):
        arr.append(int(input().strip()))
    min_val, satis, diffValsA = compute_statistics(arr)
    print(min_val, satis, diffValsA )

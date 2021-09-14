import heapq
import sys
left, right=[],[]
n = int(input())

for i in range(n):
    num = int(sys.stdin.readline())
    if len(left)==len(right):
        heapq.heappush(left,(-num,num))
    else:
        heapq.heappush(right,(num,num))
    if right and left[0][1]>right[0][1]:
        left_max=heapq.heappop(left)[1]
        right_min=heapq.heappop(right)[1]
        heapq.heappush(left,(-right_min,right_min))
        heapq.heappush(right,(left_max,left_max))
    print(left[0][1])
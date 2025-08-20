from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
q = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if q.empty():
            print(0)
        else:
            temp = q.get()
            print(temp[1])
            
    else:
        q.put((abs(request), request))
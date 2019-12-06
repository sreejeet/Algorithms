import heapq
from random import randrange

start = 1
end = 20

heap = []
order = []
heapq.heapify(heap)

while len(heap) <= end-start-1:
    x = randrange(start, end)
    heapq.heappush(heap, x)
    order.append(x)

print(f"Inserted in order {order}")
del order

l = len(heap)/2
print("Popping half the elements")
while len(heap) > l:
    print(f"{heapq.heappop(heap)}", end=' ')
else:
    print()

print(f"Remaining elements in heap\n{heap}")

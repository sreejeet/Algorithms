from math import floor
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Inserting at end
        self.heap.append(value)

        # Now moving up while lesser than parent
        pos = len(self.heap)-1
        if pos != -1:
            parent = floor(pos/2)
            while self.heap[pos] < self.heap[parent]:
                self.heap[parent], self.heap[pos] = self.heap[pos], self.heap[parent]
                pos = parent
                parent = floor(pos/2)

    def traverse(self):
        return self.heap


if __name__ == '__main__':

    from random import randrange

    start = 1
    end = 10
    heap = MinHeap()

    #  Random insertion
    nums = []
    while len(nums) <= end-start-1:
        x = randrange(start, end)
        if x not in nums:
            heap.insert(x)
            nums.append(x)

    print(f"Inserted in order {nums}")
    heapq.heapify(nums)
    
    print(nums)
    print(heap.traverse())
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

    def pop(self):
        if not self.heap:
            print('Empty heap')

        val = self.heap[0]

        # Moved last element to the top
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]

        # Moving top element to bottom
        # if greater than children
        pos = 0
        l_child = (2*pos) + 1
        r_child = (2*pos) + 2
        hl = len(self.heap)
        while True:
            if l_child < hl and self.heap[l_child] < self.heap[pos]:
                self.heap[l_child], self.heap[pos] = self.heap[pos], self.heap[l_child]
                pos = l_child
            elif r_child < hl and self.heap[r_child] < self.heap[pos]:
                self.heap[r_child], self.heap[pos] = self.heap[pos], self.heap[r_child]
                pos = r_child
            else:
                break
            l_child = (2*pos) + 1
            r_child = (2*pos) + 2

        return val

    def traverse(self):
        return self.heap

    def is_empty(self):
        return self.heap == []


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
    while not heap.is_empty():
        print(heap.pop())
        print(heap.traverse())


"""
Inserted in order [8, 7, 9, 6, 3, 1, 5, 4, 2]
[1, 2, 5, 4, 3, 9, 8, 7, 6]
[1, 2, 3, 4, 6, 7, 8, 5, 9]

Inserted in order [4, 3, 2, 5, 9, 7, 1, 8, 6]
[1, 3, 2, 5, 9, 7, 4, 8, 6]
[1, 2, 4, 3, 6, 7, 5, 8, 9]
1
[2, 3, 4, 8, 6, 7, 5, 9]
2
[3, 8, 4, 9, 6, 7, 5]
3
[4, 8, 5, 9, 6, 7]
4
[5, 8, 7, 9, 6]
5
[6, 8, 7, 9]
6
[8, 9, 7]
8
[7, 9]
7
[9]
9
[]






"""
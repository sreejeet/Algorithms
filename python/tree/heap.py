from math import floor
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def traverse(self):
        if self.is_empty():
            print('Empty heap')
            return []

        return self.heap

    def is_empty(self):
        return self.heap == []

    def get(self):
        if self.is_empty():
            print('Empty heap')
            return
        return self.heap[0]

    def length(self):
        return len(self.heap)

    def insert(self, value):
        # Inserting at end
        self.heap.append(value)

        # Now moving up while lesser than parent
        pos = len(self.heap)-1
        parent = floor(pos/2)
        hl = len(self.heap)
        while parent >= 0 and parent < hl and self.heap[pos] < self.heap[parent]:
            self.heap[parent], self.heap[pos] = self.heap[pos], self.heap[parent]
            pos = parent
            parent = floor(pos/2)

    def pop(self):
        if self.is_empty():
            print('Empty heap')
            return

        # popping the value at the top
        val = self.heap[0]

        # Moved last element to the top
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]

        # Moving top element to bottom
        # if greater than children
        pos = 0
        l_child = (2*pos)
        r_child = (2*pos)+1
        hl = len(self.heap)

        while l_child < hl:
            if r_child < hl:
                successor = l_child if self.heap[l_child] < self.heap[r_child] else r_child
            else:
                successor = l_child
            if self.heap[successor] < self.heap[pos]:
                self.heap[successor], self.heap[pos] = self.heap[pos], self.heap[successor]
                pos = successor
                l_child = (2*pos)
                r_child = (2*pos)+1
            else:
                break

        return val

if __name__ == '__main__':

    from random import randrange

    start = 1
    end = 20
    heap = MinHeap()

    # Random insertion
    nums = []
    while len(nums) <= end-start-1:
        x = randrange(start, end)
        if x not in nums:
            heap.insert(x)
            nums.append(x)

    # Iterative insertion
    # nums = [4, 2, 7, 5, 8, 6, 3, 10, 11, 9]
    # for x in nums:
    #     heap.insert(x)

    print(f"Inserted in order {nums}")

    print(heap.traverse())
    hl = heap.length()
    while heap.length() > hl/2:
        heap.pop()
        print(heap.traverse())

    print(f"Lenght of heap is {heap.length()}")
    print(f"Smallest value in heap is {heap.get()}")


""" Output
Inserted in order [13, 7, 11, 16, 17, 19, 15, 14, 10, 9, 4, 3, 6, 1, 5, 18, 12, 2, 8]
[1, 2, 3, 4, 7, 9, 6, 5, 11, 8, 19, 10, 16, 14, 15, 18, 17, 12, 13]
[2, 3, 7, 4, 8, 9, 6, 5, 11, 13, 19, 10, 16, 14, 15, 18, 17, 12]
[3, 4, 7, 5, 8, 9, 6, 12, 11, 13, 19, 10, 16, 14, 15, 18, 17]
[4, 5, 7, 6, 8, 9, 14, 12, 11, 13, 19, 10, 16, 17, 15, 18]
[5, 6, 7, 12, 8, 9, 14, 15, 11, 13, 19, 10, 16, 17, 18]
[6, 7, 8, 12, 11, 9, 14, 15, 18, 13, 19, 10, 16, 17]
[7, 8, 9, 12, 11, 10, 14, 15, 18, 13, 19, 17, 16]
[8, 9, 10, 12, 11, 16, 14, 15, 18, 13, 19, 17]
[9, 10, 11, 12, 13, 16, 14, 15, 18, 17, 19]
[10, 11, 13, 12, 17, 16, 14, 15, 18, 19]
[11, 12, 13, 14, 17, 16, 19, 15, 18]
Lenght of heap is 9
Smallest value in heap is 11
"""
from math import floor


def heapsort(arr):
    heap = []
    res = []

    for x in arr:
        heap.append(x)
        pos = len(heap)-1
        parent = floor(pos/2)
        hl = len(heap)
        while parent >= 0 and parent < hl and heap[pos] < heap[parent]:
            heap[parent], heap[pos] = heap[pos], heap[parent]
            pos = parent
            parent = floor(pos/2)

    print(f"Heap    : {heap}")

    while heap:
        res.append(heap[0])

        heap[0] = heap[-1]
        heap = heap[:-1]

        pos = 0
        l_child = (2*pos)
        r_child = (2*pos)+1
        hl = len(heap)

        while l_child < hl:
            if r_child < hl:
                successor = l_child if heap[l_child] < heap[r_child] else r_child
            else:
                successor = l_child
            if heap[successor] < heap[pos]:
                heap[successor], heap[pos] = heap[pos], heap[successor]
                pos = successor
                l_child = (2*pos)
                r_child = (2*pos)+1
            else:
                break

    return res


if __name__ == '__main__':

    from random import randrange

    start = 1
    end = 20

    nums = []
    while len(nums) <= end-start-1:
        x = randrange(start, end)
        if x not in nums:
            nums.append(x)

    print(f"Unsorted: {nums}")
    nums = heapsort(nums)
    print(f"Sorted  : {nums}")


""" Output
Unsorted: [5, 19, 1, 10, 6, 11, 8, 2, 3, 13, 16, 17, 9, 12, 15, 4, 18, 7, 14]
Heap    : [1, 2, 3, 4, 6, 11, 9, 5, 7, 13, 16, 17, 10, 12, 15, 8, 19, 18, 14]
Sorted  : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
"""
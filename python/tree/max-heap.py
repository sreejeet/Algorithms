class MaxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, val):

        # Add the new element to the end of the heap
        self.heap.append(val)

        c = len(self.heap)-1
        p = c//2

        # Adjust the element towars the top
        while self.heap[c] > self.heap[p]:
            self.heap[c], self.heap[p] = self.heap[p], val
            c = p
            p = c//2

    def peek(self):
        return self.heap[0] if self.heap else None

    def pop(self):
        if not self.heap:
            return

        return_val = self.heap[0]

        if len(self.heap) == 1:
            self.heap = []
            return return_val

        # hoist smallest element
        self.heap[0] = self.heap.pop()
        MAX_I = len(self.heap)

        # adjust the smallest element downwards
        c = 0
        while True:
            l_c = ((c+1)*2) - 1
            r_c = ((c+1)*2)

            # ss will be the max of current, left, right
            if l_c < MAX_I and self.heap[l_c] > self.heap[c]:
                ss = l_c
            else:
                ss = c
            if r_c < MAX_I and self.heap[r_c] > self.heap[ss]:
                ss = r_c

            # swap if current is less than the max of current, left right
            # else heap is satisfied
            if self.heap[c] < self.heap[ss]:
                self.heap[c], self.heap[ss] = self.heap[ss], self.heap[c]
                c = ss
            else:
                break

        return return_val


if __name__ == "__main__":

    h = MaxHeap()

    # for x in [5, 4, 6, 3, 7, 9]:
    for x in [0, 1, 9, 2, 8, 3, 7, 4, 6, 5]:
        h.insert(x)
        print(h.heap)

    print(h.peek())

    while h.heap:
        print(h.heap)
        print(h.pop())
    print(h.heap)

    print(h.peek())

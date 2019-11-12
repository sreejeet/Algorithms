class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setNext(self, new_next):
        self.next = new_next

    def setPrev(self, new_prev):
        self.prev = new_prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        self.head = node

    def setTail(self, node):
        self.tail = node

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def insert_to_empty(self, node):
        """ For internal use only """
        self.setHead(node)
        self.setTail(node)
        return True

    def insert_at_head(self, value):
        new_node = Node(value)
        if self.getHead() is None:
            return self.insert_to_empty(new_node)
        new_node.setNext(self.getHead())
        self.head.setPrev(new_node)
        self.setHead(new_node)
        return True

    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.getTail() is None:
            return self.insert_to_empty(new_node)
        new_node.setPrev(self.getTail())
        self.tail.setNext(new_node)
        self.setTail(new_node)
        return True

    def insert_after_item(self, x, value):
        if self.getHead() is None:
            print("Empty list!")
            return False
        else:
            current = self.getHead()
            while current:
                if current.getValue() == x:
                    break
                current = current.getNext()
            if current is None:
                print("Item not found")
                return False
            else:
                new_node = Node(value, current.getNext(), current)
                current.setNext(new_node)
                if self.getTail() == current:
                    self.setTail(new_node)
                else:
                    current.getNext().setPrev(new_node)
                return True

    def insert_before_item(self, x, value):
        if self.getHead() is None:
            print("Empty list!")
            return False
        else:
            current = self.getHead()
            while current:
                if current.getValue() == x:
                    break
                current = current.getNext()
            if current is None:
                print("Item not found")
            else:
                new_node = Node(value, current, current.getPrev())
                current.setPrev(new_node)
                if self.getHead() == current:
                    self.setHead(new_node)
                else:
                    current.getPrev().setNext(new_node)
                return True

    def delete_at_head(self):
        if self.getHead() is None:
            print("Empty list!")
            return False
        if self.getHead().getNext():
            self.getHead().getNext().setPrev(None)
        self.setHead(self.getHead().getNext())
        return True

    def delete_at_tail(self):
        if self.getTail() is None:
            print("Empty list!")
            return False
        if self.getTail().getPrev():
            self.getTail().getPrev().setNext(None)
        self.setTail(self.getTail().getPrev())
        return True

    def delete(self, value):
        current = self.getHead()
        while current:
            if current.getValue() == value:
                break
            current = current.getNext()
        if current is None:
            print("Empty list!")
            return False
        if current is self.getHead():
            return self.delete_at_head()
        if current is self.getTail():
            return self.delete_at_tail()
        current.getNext().setPrev(current.getPrev())
        current.getPrev().setNext(current.getNext())
        return True

    def traverse(self):

        forward = []
        current = self.getHead()
        while current:
            forward.append(current.getValue())
            current = current.getNext()

        backward = []
        current = self.getTail()
        while current:
            backward.append(current.getValue())
            current = current.getPrev()

        # An internal check
        if forward != backward[::-1]:
            print(forward)
            print(backward[::-1])
            raise ValueError("Forward and backward traversals do not match!")

        print(forward)


if __name__ == '__main__':

    ll = DoublyLinkedList()

    for x in range(10):
        """ Sort even values to the left. """
        if x % 2 == 0:
            ll.insert_at_head(x)
        else:
            ll.insert_at_tail(x)

    ll.delete(7)

    ll.insert_after_item(9, 11)
    ll.insert_at_tail(13)

    ll.insert_before_item(8, 10)
    ll.insert_at_head(12)

    ll.traverse()


""" Output
[12, 10, 8, 6, 4, 2, 0, 1, 3, 5, 9, 11, 13]
"""
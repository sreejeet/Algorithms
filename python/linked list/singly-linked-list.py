class Node(object):

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.next_node

    def setNext(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.setNext(self.head)
        self.head = new_node

    def search(self, value):
        current = self.head
        counter = 0
        while current:
            counter += 1
            if current.getValue() == value:
                break
            current = current.getNext()
        if current is None:
            print(f"{value} not found.")
            return False
        print(f"Found {value} at node {counter}.")
        return True

    def update(self, value, new_value):
        current = self.head
        counter = 0
        while current:
            counter += 1
            if current.getValue() == value:
                break
            current = current.getNext()
        if current is None:
            print(f"{value} not found.")
            return False
        current.setValue(new_value)
        print(f"Updated {value} to {new_value} at node {counter}.")
        return True

    def delete(self, value):
        current = self.head
        previous = None
        counter = 0
        while current:
            counter += 1
            if current.getValue() == value:
                break
            previous = current
            current = current.getNext()
        if current is None:
            print(f"{value} not found.")
            return False
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        print(f"Deleted {value} at {counter}")
        return True

    def traverse(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            print(f"{current.getValue()}", end=' ')
            current = current.getNext()
        print()

    def reverse(self):
        if self.head == None:
            print("Cannot reverse empty linked list")
            return

        prev_n = self.head
        next_n = self.head.next_node
        self.head.next_node = None

        while next_n:
            tmp = next_n
            next_n = next_n.next_node
            tmp.next_node = prev_n
            prev_n = tmp

        self.head = prev_n


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(2)
    ll.traverse()

    ll.search(5)

    ll.insert(5)
    ll.traverse()

    ll.search(5)

    ll.delete(2)
    ll.traverse()

    ll.search(1)
    ll.search(2)

    ll.delete(5)
    ll.traverse()

    ll.search(3)

    ll.update(3, 33)
    ll.traverse()

    ll.reverse()
    ll.traverse()

""" Output
2 3 2 1 
5 not found.
5 2 3 2 1 
Found 5 at node 1.
Deleted 2 at 2
5 3 2 1 
Found 1 at node 4.
Found 2 at node 3.
Deleted 5 at 1
3 2 1 
Found 3 at node 1.
Updated 3 to 33 at node 1.
33 2 1 
"""

class Node(object):

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def getValue(self):
        return self.value

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
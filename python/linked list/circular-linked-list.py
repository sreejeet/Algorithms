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


class CircularLinkedList: 

    def __init__(self): 
        self.head = None

    def setHead(self, node):
        self.head = node

    def getHead(self):
        return self.head

    def len(self):
        head = self.getHead()
        current = self.getHead()
        counter = 0
        while current:
            counter += 1
            current = current.getNext()
            if current == head:
                break
        return counter

    def insert(self, value):
        new_node = Node(value)
        if self.getHead() is None:
            self.setHead(new_node)
        new_node.setNext(self.getHead())
        current = self.getHead()
        while current:
            current = current.getNext()
            if current.getNext() == self.getHead():
                break
        current.setNext(new_node)
        self.setHead(new_node)

    def delete(self, value):
        head = self.getHead()
        current = self.getHead()

        if head.getValue() == value and head == head.getNext():
            self.setHead(None)
            return True

        if head.getValue() == value:
            while current.getNext() != head:
                current = current.getNext()
            current.setNext(head.getNext())
            self.setHead(current.getNext())
            return True

        current = head
        while True:
            if current.getNext().getValue() == value:
                current.setNext(current.getNext().getNext())
                return True
            current = current.getNext()
            if current == head:
                break
        
        return False

    def traverse(self):
        head = self.getHead()
        current = head
        counter = 0
        while current:
            counter += 1
            print(f"{current.getValue()}", end=' ')
            current = current.getNext()
            if current == head:
                break
        print()



ll = CircularLinkedList()
ll.insert(3)
ll.traverse()
ll.insert(2)
ll.traverse()
ll.insert(1)
ll.traverse()
ll.delete(3)
ll.traverse()
ll.delete(1)
ll.traverse()
ll.delete(2)
ll.traverse()


""" Output
3 
2 3 
1 2 3 
1 2 
2 

"""
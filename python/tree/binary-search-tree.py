class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = None

    def insert(self, value, node=None):
        if not self.root:
            self.root = Node(value)
            return

        if not node:
            node = self.root

        if value > node.value:
            if node.right:
                self.insert(value, node.right)
            else:
                node.right = Node(value)
        elif value < node.value:
            if node.left:
                self.insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            print(f"{value} already exists")

    def search(self, value, node=None):
        if not self.root:
            print("Empty tree")
            return

        if not node:
            node = self.root

        if value > node.value and node.right:
            return self.search(value, node.right)
        elif value <  node.value and node.left:
            return self.search(value, node.left)
        elif value == node.value:
            return node
        print(f"Node with value {value} not found")
        return None

    def len(self, node=None):
        if not self.root:
            return 0

        if not node:
            node = self.root

        len = 1
        if node.left:
            len += self.len(node.left)
        if node.right:
            len += self.len(node.right)

        return len

    def height(self, node=None):
        if not self.root:
            return 0

        if not node:
            node = self.root

        hl = 0
        hr = 0
        if node.left:
            hl += self.height(node.left)
        if node.right:
            hr += self.height(node.right)

        return 1 + max(hl, hr)

    def min(self, current=None):
        if not self.root:
            print("Empty tree")
            return

        if not current:
            current = self.root

        if current.left:
            return self.min(current.left)
        return current

    def max(self, current=None):
        if not self.root:
            print("Empty tree")
            return

        if not current:
            current = self.root

        if current.right:
            return self.max(current.right)
        return current

    def delete(self, value, node=None, parent=None, relation='orphan', message='Deleted'):
        if not self.root:
            print("Empty tree")
            return

        if not node:
            node = self.root

        while node:

            if node.value == value:
                if node.left or node.right:
                    if node.left:
                        replace = self.max(node.left)
                        new_val = replace.value
                        self.delete(replace.value, node.left, node, 'left', 'Moved')
                        node.value = new_val
                    else:
                        replace = self.min(node.right)
                        new_val = replace.value
                        self.delete(replace.value, node.right, node, 'right', 'Moved')
                        node.value = new_val
                else:
                    if relation == 'left':
                        parent.left = None
                    elif relation == 'right':
                        parent.right = None
                    elif relation == 'orphan':
                        self.root = node.left

                print(f"{message} {value}, child of {parent.value if parent else 'no one'}, related as {relation}")
                return

            parent = node
            if value > node.value:
                relation = 'right'
                node = node.right
            else:
                relation = 'left'
                node = node.left

        print(f"Node with value {value} not found")

    def traverse(self, order='inorder', current=None):
        if not self.root:
            print("Empty tree")
            return

        if not current:
            current=self.root

        if order=='preorder':
            print(current.value)
        if current.left:
            self.traverse(order, current.left)
        if order=='inorder':
            print(current.value)
        if current.right:
            self.traverse(order, current.right)
        if order=='postorder':
            print(current.value)


if __name__=='__main__':

    from random import randrange, choice

    """ 
    Max recursion depth is 1000.
    End is exclusive
    """
    start = 0
    end = 20
    tree = BinarySearchTree()

    #  Random insertion
    nums = []
    while len(nums) <= end-start-1:
        x = randrange(start, end)
        if x not in nums:
            tree.insert(x)
            nums.append(x)

    # Tree info
    print(f"Inserted in order\n{nums}")
    print(f"Min and max are {tree.min().value} and {tree.max().value}")
    print(f"Height of tree is {tree.height()}")
    print(f"Total nodes: {tree.len()}")

    # Deletions
    for x in [(start + end) // 2, start, end-1]:
        print()
        node = tree.search(x)
        tree.delete(node.value)
        print(f"{tree.root.value}")
        print(f"Total nodes: {tree.len()}")

    print(f"Traversing inorder:")
    tree.traverse()


""" Output
Inserted in order
[0, 10, 1, 17, 8, 9, 13, 11, 12, 14, 18, 6, 2, 19, 3, 4, 16, 7, 15, 5]
Min and max are 0 and 19
Height of tree is 9
Total nodes: 20

Moved 9, child of 8, related as right
Deleted 10, child of 0, related as right
0
Total nodes: 19

Moved 5, child of 4, related as right
Moved 4, child of 3, related as right
Moved 3, child of 2, related as right
Moved 2, child of 6, related as left
Moved 1, child of 9, related as left
Deleted 0, child of no one, related as orphan
1
Total nodes: 18

Deleted 19, child of 18, related as right
1
Total nodes: 17
Traversing inorder:
1
2
3
4
5
6
7
8
9
11
12
13
14
15
16
17
18
"""
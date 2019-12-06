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

    def traverse_levelorder(self):
        if not self.root:
            print("Empty tree")
            return

        q = [self.root]
        while q:
            current = q.pop(0)
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)


if __name__=='__main__':

    from random import randrange

    """ 
    Max recursion depth is 1000.
    End is exclusive
    """
    start = 1
    end = 20
    tree = BinarySearchTree()

    #  Random insertion
    nums = []
    while len(nums) <= end-start-1:
        x = randrange(start, end)
        if x not in nums:
            tree.insert(x)
            nums.append(x)

    #  Iterative insertion
    # nums = [13, 19, 2, 11, 3, 7, 14, 6, 12, 16, 1, 9, 18, 17, 15, 4, 10, 8, 5]
    # for x in nums:
    #     tree.insert(x)

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

    print(f"Traversing levelorder:")
    tree.traverse_levelorder()



""" Output
Inserted in order
[18, 13, 12, 7, 17, 16, 2, 14, 3, 6, 5, 9, 11, 1, 15, 4, 8, 10, 19]
Min and max are 1 and 19
Height of tree is 9
Total nodes: 19

Deleted 10, child of 11, related as left
18
Total nodes: 18

Deleted 1, child of 2, related as left
18
Total nodes: 17

Deleted 19, child of 18, related as right
18
Total nodes: 16
Traversing inorder:
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
Traversing levelorder:
18
13
12
17
7
16
2
9
14
3
8
11
15
6
5
4
"""
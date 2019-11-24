class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    root = None

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
        else:
            if node.left:
                self.insert(value, node.left)
            else:
                node.left = Node(value)

    def search(self, value, node=None):
        if not self.root:
            print("Empty tree")
            return

        if not node:
            node = self.root

        if value > node.value and node.right:
            return self.search(value, node.right)
        if value < node.value and node.left:
            return self.search(value, node.left)
        if value == node.value:
            print(f"Found {value}")
            return node

        print(f"Node with value {value} not found")

    def min(self, current=None):
        if not self.root:
            print("Empty tree")
            return

        if not current:
            current = self.root

        if current.left:
            return self.min(current.left)
        return current.value

    def max(self, current=None):
        if not self.root:
            print("Empty tree")
            return

        if not current:
            current = self.root

        if current.right:
            return self.max(current.right)
        return current.value

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

    def delete(self, value):
        # TODO
        pass

if __name__=='__main__':

    from random import randrange, choice

    """ 
    Max recursion depth is 1000.
    End is exclusive
    """
    start = -5
    end = 5
    tree = BinaryTree()
    nums = []

    while len(nums) <= end-start-1:
        x = randrange(start, end)
        if x not in nums:
            tree.insert(x)
            nums.append(x)

    print(f"Inserted in order\n{nums}")

    print("Traversing preorder:")
    tree.traverse('preorder')

    print("Traversing inorder:")
    tree.traverse('inorder')

    print("Traversing postorder:")
    tree.traverse('postorder')

    print(f"Min is {tree.min()}")
    print(f"Max is {tree.max()}")
    node = tree.search(2)


""" Output
Inserted in order
[0, -5, 3, -2, -4, -1, 4, 2, -3, 1]
Traversing preorder:
0
-5
-2
-4
-3
-1
3
2
1
4
Traversing inorder:
-5
-4
-3
-2
-1
0
1
2
3
4
Traversing postorder:
-3
-4
-1
-2
-5
1
2
4
3
0
Min is -5
Max is 4
Found 2
"""
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
                        replace = self.min(node.left)
                        new_val = replace.value
                        self.delete(replace.value, node.left, node, 'left', 'Moved')
                        node.value = new_val
                        # print("D1")
                    else:
                        replace = self.min(node.right)
                        new_val = replace.value
                        self.delete(replace.value, node.right, node, 'right', 'Moved')
                        node.value = new_val
                        # print("D2")
                else:
                    if relation == 'left':
                        parent.left = None
                        # print("D3")
                    else:
                        parent.right = None
                        # print("D4")

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

if __name__=='__main__':

    from random import randrange, choice

    """ 
    Max recursion depth is 1000.
    End is exclusive
    """
    # for iteration in range(100000):
    start = 0
    end = 20
    tree = BinarySearchTree()

    #  Random insertion
    # nums = []
    # while len(nums) <= end-start-1:
    #     x = randrange(start, end)
    #     if x not in nums:
    #         tree.insert(x)
    #         nums.append(x)

    # Ordered insertion
    # nums = [0, 17, 1, 6, 9, 7, 3, 5, 14, 12, 15, 16, 10, 11, 4, 19, 8, 18, 2, 13]
    # nums = [3, 5, 7, 4, 8, 13, 17, 6, 9, 15, 10, 11, 16, 0, 14, 19, 18, 1, 12, 2]
    # nums = [15, 16, 2, 18, 9, 0, 10, 1, 19, 6, 17, 5, 13, 11, 14, 3, 7, 12, 8, 4]
    # nums = [0, 3, 4, 2, 1]
    # Bug in these inputs:
    nums = [19, 5, 9, 3, 0, 18, 8, 15, 12, 4, 2, 13, 6, 1, 10, 7, 16, 17, 14, 11]
    # nums = [14, 16, 2, 6, 10, 13, 19, 5, 15, 12, 11, 7, 4, 9, 0, 3, 1, 18, 8, 17]
    for x in nums:
        tree.insert(x)

    print(f"Inserted in order\n{nums}")
    # print(f"Min and max are {tree.min().value} and {tree.max().value}")
    # print(f"Height of tree is {tree.height()}")

    print(f"Total nodes: {tree.len()}")

    # Deletions
    for x in [(start + end) // 2, start, end-1]:
        print()
        node = tree.search(x)
        tree.delete(node.value)
        print(f"{tree.root.value}")
        print(f"Total nodes: {tree.len()}")


    # print(f"{iteration+1}. Traversing inorder:")
    tree.traverse()


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
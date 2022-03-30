class BinaryTreeNode:
    """
    Recursive BinaryTreeNode that holds info on its data, left, right and parent node.
    """
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        """Inserts a number into the BinaryTree. If duplicate the insert will be ignored.

        :param value: Integer - the value to insert
        """
        if self.data == value:
            return

        if value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinaryTreeNode(value)
                self.left.parent = self
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinaryTreeNode(value)
                self.right.parent = self

    def delete(self, value):
        """Deletes a number from the BinaryTree and shrinks the tree from the right.

        :param value: Integer - the value to delete.
        """
        if value == self.data:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                self.right.parent = self.parent
                return self.right
            elif self.right is None:
                self.left.parent = self.parent
                return self.left

            # update tree from right side
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
            # can also update tree from left side using self.left.find_max()
        elif value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)

        return self

    def find_min(self):
        """
        Finds the minimum value after the node it is called on.
        """
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        """
        Finds the maximum value after the node it is called on.
        """
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def search(self, value):
        """Binary search the tree for a given value.

        :param value: Integer - the value to look for.
        :return: Boolean - True if found, False if not.
        """
        if self.data == value:
            return True
        else:
            if value < self.data:
                if self.left:
                    return self.left.search(value)
                else:
                    return False
            else:
                if self.right:
                    return self.right.search(value)
                else:
                    return False

    def in_order_traversal(self):
        """Traverses the tree from left to right. (left -> root -> right)

        :return: List - list of numbers ordered.
        """
        result_list = []
        if self.left:
            result_list += self.left.in_order_traversal()
        result_list.append(self.data)
        if self.right:
            result_list += self.right.in_order_traversal()

        return result_list

    def pre_order_traversal(self):
        """Traverses the tree in pre order (root -> left -> right)

        :return: List - list of numbers ordered.
        """
        result_list = [self.data]
        if self.left:
            result_list += self.left.pre_order_traversal()
        if self.right:
            result_list += self.right.pre_order_traversal()

        return result_list

    def post_order_traversal(self):
        """Traverses the tree in post order (left -> right -> root)

        :return: List - list of numbers ordered.
        """
        result_list = []
        if self.left:
            result_list += self.left.post_order_traversal()
        if self.right:
            result_list += self.right.post_order_traversal()
        result_list.append(self.data)

        return result_list

    def get_level(self):
        """Returns the level of the node in the tree, for printing purposes.

        :return: Integer - the level where the nod is at.
        """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_binary_tree(self):
        """
        Prints the BinaryTree horizontally.
        """
        prefix = ' ' * self.get_level() * 3 + "-->{}" if self.parent else "-->{}"
        print(prefix.format(self.data))
        if self.right:
            self.right.print_binary_tree()
        if self.left:
            self.left.print_binary_tree()


def build_tree_from_list(numbers_list):
    """Builds a BinaryTree from a list of integers. The first element is always the root.

    :param numbers_list: List - list of numbers to build the tree from
    :return:
    """
    if len(numbers_list) > 0:
        binary_tree = BinaryTreeNode(numbers_list[0])

        for i in range(1, len(numbers_list)):
            binary_tree.insert(numbers_list[i])

        return binary_tree

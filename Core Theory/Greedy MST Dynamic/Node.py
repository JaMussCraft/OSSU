class Node():
    def __init__(self, symbol):
        self.parent = None
        self.node = symbol
        self.left = None
        self.right = None

    @classmethod
    def insert(self, parent, child):
        if parent.get_left() != None and parent.get_right() != None:
            print('Both left and right are full, cannot insert anymore!')
            raise RuntimeError
        elif parent.get_left() == None:
            parent.insert_left(child)
            child.insert_parent(parent)

        elif parent.get_right() == None:
            parent.insert_right(child)
            child.insert_parent(parent)

        else:
            print('HELP ME, extra ignored case!')
            raise RuntimeError

    @classmethod
    def replace(self, parent, old_child, new_child):
        if parent.get_left() == old_child:
            new_child.insert_parent(parent)
            parent.left = new_child

        elif parent.get_right() == old_child:
            new_child.insert_parent(parent)
            parent.right = new_child

        else:
            print(f'Parent {parent} does not have an old child called\
                  {old_child}')

    def get_parent(self):
        return self.parent

    def get_left(self):

        return self.left

    def get_right(self):
        return self.right

    def insert_left(self, node):
        if self.left != None:
            print('Left node already occupied!')
            raise RuntimeError

        self.left = node

    def insert_right(self, node):
        if self.right != None:
            print('Right node already occupied!')
            raise RuntimeError

        self.right = node

    def insert_parent(self, node):
        if self.parent != None:
            print('Parent node already occupied!')
            raise RuntimeError

        self.parent = node

    def __str__(self):
        return str(self.node)

    # search for node with the given symbol, if not found return None
    def search(self, symbol):
        if self.node == symbol:
            return self
        else:
            if self.left != None:
                left_result = self.left.search(symbol)
            else:
                left_result = None

            if self.right != None:
                right_result = self.right.search(symbol)
            else:
                right_result = None

            if left_result == None and right_result == None:
                return None

            elif left_result != None:
                return left_result

            elif right_result != None:
                return right_result

        return None

    # print the tree starting from this node
    def print_tree(self, level=0):
        result = "  "*level+str(self.node)+"\n"

        if self.left != None:
            left_result = self.left.print_tree(level+1)
            result += left_result

        if self.right != None:
            right_result = self.right.print_tree(level+1)
            result += right_result

        return result

    # return the depth of the the tree starting from this node
    def get_depth(self, level=0):
        result = level

        if self.left != None:
            left_level = self.left.get_depth(level+1)
            result = max(result, left_level)

        if self.right != None:
            right_level = self.right.get_depth(level+1)
            result = max(result, right_level)

        return result

    def get_min_depth(self, level=0):
        if self.left == None and self.right == None:
            return level

        if self.left != None:
            left_level = self.left.get_min_depth(level+1)
        else:
            left_level = None

        if self.right != None:
            right_level = self.right.get_min_depth(level+1)
        else:
            right_level = None

        if left_level != None and right_level != None:
            return min(left_level, right_level)
        elif left_level != None:
            return left_level
        else:
            return right_level

        


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_100 = Node(100)

    Node.insert(node_1, node_4)
    Node.insert(node_1, node_3)
    Node.insert(node_4, node_6)
    Node.insert(node_3, node_2)
    Node.insert(node_3, node_5)

    print(node_1.print_tree())
    print(node_1.get_min_depth(), 'min depth')

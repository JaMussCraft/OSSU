import sys
from Node import Node
sys.setrecursionlimit(3000)

# create a subtree from the two given symbols
def create_subtree(symbol_1, symbol_2):
    global depth
    depth += 1

    node_random = Node(-1)
    node_1 = Node(symbol_1)
    node_2 = Node(symbol_2) 

    node_random.insert_left(node_1)
    node_1.insert_parent(node_random)
    node_random.insert_right(node_2)
    node_2.insert_parent(node_random)

    # return the root of the subtree
    return node_random


# symbols is a list of weights of the symbols
def huffman(symbols):

    # base case: 2 symbols
    if len(symbols) == 2:
        
        symbol_1 = symbols[0]
        symbol_2 = symbols[1]

        root_subtree = create_subtree(symbol_1, symbol_2)

        return root_subtree

    else: # normal case
        # find the two smallest weights from symbols
        symbol_1 = None
        weight_1 = 999999999999
        symbol_2 = None
        weight_2 = 999999999999
        for symbol in symbols:
            weight = symbol_to_weight[symbol]
            if weight < weight_1:
                weight_1 = weight
                symbol_1 = symbol

        symbols.remove(symbol_1)

        for symbol in symbols:
            weight = symbol_to_weight[symbol]
            if weight < weight_2:
                weight_2 = weight
                symbol_2 = symbol

        symbols.remove(symbol_2)

        # update the weights and append the new meta symbol into symbols
        symbol_to_weight[symbol_1,symbol_2] = weight_1 + weight_2
        new_symbol = (symbol_1,symbol_2)
        symbols.append(new_symbol)

        # create a subtree from the two symbols
        uncompressed_subtree = create_subtree(symbol_1, symbol_2)

        compressed_subtree = huffman(symbols)

        # find the correct leaf of compressed subtree and replace it with
        # uncompressed subtree
        leaf = compressed_subtree.search(new_symbol)
        leaf_parent = leaf.get_parent()
        Node.replace(leaf_parent, leaf, uncompressed_subtree)

        return compressed_subtree








def main():
    global depth, symbol_to_weight
    # depth is the number of times merge happens or huffman called
    depth = 0
    num_of_symbols = None
    # dict mapping symbol index to its weight
    symbol_to_weight = {}
    symbols = []

    with open('Core Theory/Greedy MST Dynamic/huffman.txt', 'r') as file:
        first_line = True
        i = 1

        for line in file:
            num = int(line.strip())

            if not first_line:
                symbols.append(i)
                symbol_to_weight[i] = num
                i += 1

            else:
                num_of_symbols = num
                first_line = False

    #symbols = [1,2,3,4,5]

    tree = huffman(symbols)
    print(tree.print_tree()) 
    print(f'Depth is {tree.get_min_depth()}')



            


if __name__ == '__main__':
    main()
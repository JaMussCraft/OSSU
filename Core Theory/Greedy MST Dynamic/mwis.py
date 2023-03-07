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
    num_of_nodes = None
    # nodes[i] return node i's weight
    nodes = [-1]
    # return the solution to the first <array index> number of nodes
    # example: solutions[2] return the solution to the
    # subgraph formed from node 1 and node 2
    solutions = [-1 for i in range(1001)]
    # a list of nodes that corresponds to the maximum-weight independent set
    solution_set = []

    with open('Core Theory/Greedy MST Dynamic/pathgraph.txt', 'r') as file:
        first_line = True

        for line in file:
            num = int(line.strip())

            if not first_line:
                nodes.append(num)

            else:
                num_of_nodes = num
                first_line = False

    # TEST
    #nodes = [-1,4,2,4,2]
    #solutions = [-1,-1,-1,-1,-1]
    #num_of_nodes = 4

    # trivial case 1: solutions[0] = 0
    solutions[0] = 0

    # trivial case 2: solutions[1] = node 1
    solutions[1] = nodes[1]

    for i in range(2, num_of_nodes+1):
        solutions[i] = max(solutions[i-1], solutions[i-2] + nodes[i])

    # Reconstruct
    i = num_of_nodes
    while i > 0:
        # case 1: node excluded
        if solutions[i-1] > solutions[i-2] + nodes[i]:
            i -= 1
        else: # case 2: node included
            solution_set.append(i)
            i -= 2


    result = ''
    for i in [1,2,3,4,17,117,517,997]:
        if i in solution_set:
            result += '1'
        else:
            result+= '0'

    print(f'Result is {result}') # 10100110



            


if __name__ == '__main__':
    main()
from UnionFind import UnionFind

def main():
    num_node = None
    nodes = set()
    edges = []

    with open('clusters.txt', 'r') as file:
        first_line = True

        for line in file:
            data = line.split()

            if not first_line:
                n1 = int(data[0])
                n2 = int(data[1])
                c = int(data[2])

                nodes.add(n1)
                nodes.add(n2)

                edges.append((n1,n2,c))

            else: # first line
                num_node = int(data[0])
                first_line = False

    edges = [(1,3,1),(4,5,2),(6,7,3),(2,8,4),(6,2,10),(5,6,20),(5,3,30),(3,2,40)]
    num_node = 8
    union_find = UnionFind(num_node)

    # sort the edges from largest cost to lowest cost
    edges.sort(reverse=True, key=lambda x: x[2])
    print(len(edges), 'edge length')

    while union_find.get_num_clusters() > 4:
        shortest_edge = edges.pop()
        n1 = shortest_edge[0]
        n2 = shortest_edge[1]
        c = shortest_edge[2]

        if union_find.find(n1) != union_find.find(n2):
            union_find.union(n1, n2)

    print(union_find.get_clusters())


    max_space = 0
    node_1 = None
    node_2 = None
    # loop through the rest of the edges and find the one with the largest cost
    # but both of its nodes have to be in different cluster
    for edge in edges:
        if union_find.find(edge[0]) != union_find.find(edge[1]):
            if edge[2] > max_space:
                max_space = edge[2]
                node_1 = edge[0]
                node_2 = edge[1]
                print(f'{node_1} and {node_2} with cost {edge[2]} has a bigger cost')
                print(f'node 1 belongs {union_find.find(node_1)}')
                print(f'node 2 belongs {union_find.find(node_2)}')

    

    print(f'Max space is {max_space}')


if __name__ == '__main__':
    main()
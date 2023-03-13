import numpy as np
import sys
sys.setrecursionlimit(10000)

# return edge length if i and j form an edge else False
def get_edge_length(i, j, edges):
    if i in edges:
        for end in edges[i]:
            if end[0] == j:
                return end[1]
    
    return False

def APSP(n, edges):
    ss_path = 99999999999999999999

    # 3D array represented as a dict
    A = {}
    # key: i-j-k | output: value
    for k in range(n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                key = str(i) + str(j) + str(k)
                A[key] = -1
    print('here')

    
    # initial array with base cases
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j][0] = 0
            else:
                if length := get_edge_length(i+1, j+1, edges):
                    A[i][j][0] = length
                
                else: 
                    A[i][j][0] = 99999999999999999999


    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                A[i][j][k] = min(A[i][j][k-1], A[i][k][k-1] + A[k][j][k-1])
                ss_path = A[i][j][k] if A[i][j][k] < ss_path else ss_path

    return ss_path

def main():
    num_of_nodes = None
    num_of_edges = None
    # maps tail to (head, length)
    edges = {}

    with open('Core Theory/Shortest Paths Revisited and NP-Complete/graph_1.txt', 'r') as file:
        first_line = True
        for line in file:
            data = [int(x) for x in line.split()]

            if not first_line:
                tail = data[0]
                head = data[1]
                length = data[2]
                if tail in edges:
                    edges[tail].append((head, length))
                else:
                    edges[tail] = [(head, length)]

            else:
                num_of_nodes = data[0]
                num_of_edges = data[1]
                first_line = False

    #n = 2
    #edges = {
    #    1: [(2,-100)],
    #    2: [(1,500)]
    #}
    print('stared APSP')
    ss_path = APSP(num_of_nodes, edges)
    print(ss_path)

    


if __name__ == '__main__':
    main()
import numpy as np
import sys
import threading
threading.stack_size(67108864)
sys.setrecursionlimit(10000)

def re_APSP(n, k):
    print(f'started {k}')
    global edge_length, edges, ss

    # base case: when k = 0
    if k == 0:
        # 2D array for k = 0
        A = []
        for i in range(n):
            A.append([])
            for j in range(n):
                A[i].append([])
                if i == j:
                    A[i][j] = 0
                else:
                    key = str(i+1) + str(j+1)
                    if (length := edge_length.get(key)):
                        A[i][j] = length
                    
                    else: 
                        A[i][j] = 99999999999999999999
        print(f'finished {k}')
        return A

    # normal case
    else:
        old_A = re_APSP(n, k-1)

        # 2D array for the current k
        new_A = []
        for i in range(n):
            new_A.append([])
            for j in range(n):
                new_A[i].append([])
                new_A[i][j] = min(old_A[i][j], old_A[i][k] + old_A[k][j])
                ss = new_A[i][j] if new_A[i][j] < ss else ss

        # check negative cycle
        if k == n-1:
            for i in range(n):
                if new_A[i][i] < 0:
                    print('negative cost cycle found')
                    return False
                
            print(new_A)

        print(f'finished {k}')
        return new_A
    

def APSP(n, edges):
    ss_path = 99999999999999999999

    # 3D array indexed by i j k
    A = [[[-1 for i in range(n)] for i in range(n)] for i in range(n)]
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
    global edges, edge_length, ss
    num_of_nodes = None
    num_of_edges = None
    # maps tail to (head, length)
    edges = {}
    # map ij to edge_length (depend whether they form an edge)
    edge_length = {}
    ss = 99999999999999999999

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
                edge_length[str(tail)+str(head)] = length

            else:
                num_of_nodes = data[0]
                num_of_edges = data[1]
                first_line = False
    '''
    num_of_nodes = 2
    edges = {
        1: [(2,-100)],
        2: [(1,500)]
    }
    edge_length = {
        '12': -100,
        '21': 500
    }
    '''
    print('stared APSP')
    re_APSP(num_of_nodes, num_of_nodes-1)
    print(ss)

    


if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()
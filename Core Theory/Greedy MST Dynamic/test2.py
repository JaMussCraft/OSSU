import numpy as np
import sys
#import threading
sys.setrecursionlimit(3000)

def re_knapsack(i, size):
    global dict, weights, values

    key = (i, size)


    # base case: num_of_items is zero, then the answer is zero
    if i == 0:
        # cache the result
        dict[key] = 0
        return 0
    
    key_1 = (i-1, size - weights[i])
    key_2 = (i-1, size)
    # normal case:
    if size > weights[i]:

        if key_1 in dict and key_2 in dict:
            dict[key] =  max(dict[key_1] + values[i], dict[key_2]) 
        
        elif key_1 in dict:
            dict[key] = max(dict[key_1] + values[i], re_knapsack(i-1, size)) 
        
        elif key_2 in dict:
            dict[key] = max(re_knapsack(i-1, size-weights[i]) + values[i], dict[key_2]) 
        
        # trivial case: weight of the item is bigger than size
        else:
            # use bigger of the two cases
            dict[key] = max(re_knapsack(i-1, size),\
                re_knapsack(i-1, size-weights[i]) + values[i])
        
    else: # weight is bigger than the size
        if key_2 in dict:
            dict[key] = dict[key_2]

        else:
            dict[key] = re_knapsack(i-1,size)

        
    return dict[key]

def main():
    global dict, weights, values
    size = None
    num_of_items = None
    values = [-1]
    weights = [-1]
    items = [-1]
    # dict mapping (num_of_items, size) to answer
    dict = {}

    with open('Core Theory/Greedy MST Dynamic/knapsack_big.txt', 'r') as file:
        first_line = True

        for line in file:
            data = [int(x) for x in line.split()]
            value = data[0]
            weight = data[1]
  
            if not first_line:
                values.append(value)
                weights.append(weight)
                items.append((value, weight))

            else:
                first_line = False
                size = value # place holder in this case
                num_of_items = weight

    #num_of_items = 4
    #size = 6
    #values = [-1,3,2,4,4]
    #weights = [-1,4,3,2,3]
    #items = [(3,4),(2,3),(4,2),(4,3)]
    
    # subproblems with num_of_items as item, covering every size
    result = re_knapsack(num_of_items, size)

    #print(np.array(array))
    print('The answer is', result)

            


if __name__ == '__main__':
    #t1 = threading.Thread(target=main())
    #t1.start()
    main()
import numpy as np
import sys
#import threading
sys.setrecursionlimit(10000)

def re_knapsack(items, size, pre_item, cur_item):

    num_of_items = len(items) - 1

    # check if the answer is already available
    if cur_item[size] != -1:
        return cur_item[size]


    # base case: num_of_items is zero, then the answer is zero
    if num_of_items == 0:
        # cache the result
        cur_item[size] = 0
        return 0
    
    # normal case:
    else:
        # sub_items has the last item removed
        sub_items = items[:num_of_items]
        last_item = items[num_of_items]
        value = last_item[0]
        weight = last_item[1]

        # trivial case: weight of the item is bigger than size
        if weight > size:
            # use case 1
            result = re_knapsack(sub_items, size, pre_item, pre_item)
            return result
        else:
            # use bigger of the two cases
            result = max(re_knapsack(sub_items, size),\
                re_knapsack(sub_items, size - weight) + value)
    
            dict[num_of_items, size] = result
            return result

def main():
    global dict
    size = None
    num_of_items = None
    values = [-1]
    weights = [-1]
    items = [-1]
    # 2D array
    array = []
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

    num_of_items = 4
    size = 6
    values = [-1,3,2,4,4]
    weights = [-1,4,3,2,3]
    items = [(3,4),(2,3),(4,2),(4,3)]
    
    # subproblems with num_of_items as item, covering every size
    cur_item = [-1 for x in range(size+1)]
    pre_item = [0 for x in range(size+1)]
    result = re_knapsack(items, size, pre_item, cur_item)

    #print(np.array(array))
    print('The answer is', result)

            


if __name__ == '__main__':
    #t1 = threading.Thread(target=main())
    #t1.start()
    main()
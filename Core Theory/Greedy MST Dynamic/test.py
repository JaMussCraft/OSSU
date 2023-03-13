import numpy as np

def main():
    size = None
    num_of_items = None
    values = [-1]
    weights = [-1]
    # 2D array
    array = []

    with open('Core Theory/Greedy MST Dynamic/knapsack_big.txt', 'r') as file:
        first_line = True

        for line in file:
            data = [int(x) for x in line.split()]
            value = data[0]
            weight = data[1]
  
            if not first_line:
                values.append(value)
                weights.append(weight)

            else:
                first_line = False
                size = value # place holder in this case
                num_of_items = weight

    #num_of_items = 4
    #size = 6
    #values = [-1,3,2,4,4]
    #weights = [-1,4,3,2,3]


    # initialize the array
    for i in range(num_of_items+1):
        array.append([])
        for j in range(size+1):
            array[i].append([])

            if i == 0:
                array[i][j] = 0
            else:
                array[i][j] = -1


    for i in range(1, num_of_items+1): # loop through the items
        for j in range(size+1):# loop through the all the possible sizes of the subproblems
            #if i == 2 and j == 3:
            #    print('inherit', array[i-1][j])
            #    print('include', )
            if weights[i] > j:
                array[i][j] = array[i-1][j]
            else:
                array[i][j] = max(array[i-1][j], array[i-1][j-weights[i]] + values[i])
        

    #print('capacity', capacity)
    #print('num items', num_of_items)
    #print('values', values)
    #print('weights', weights)

    #print(np.array(array))
    print('The answer is', array[-1][-1])

            


if __name__ == '__main__':
    main()
file = "Core Theory/Greedy MST Dynamic/knapsack_big.txt"

fp = open(file, 'r+')

data = fp.readlines()
W, n = data[0].split(" ")
W, n = int(W), int(n)

v = []
w = []

for r in data[1:]:
    v_i, w_i = r.split(" ")
    v.append(int(v_i))
    w.append(int(w_i))

import sys
sys.setrecursionlimit(2500)

cache = dict()
def knap(i, _w):
#     print (i, _w)
    key = str(i)+"//-//"+str(_w)

    if i == 0:
        cache[key] = 0
        return 0
    
    if _w > w[i]:
        key1 = str(i-1)+"//-//"+str(_w - w[i])
        key2 = str(i-1)+"//-//"+str(_w)
        
        if key1 in cache and key2 in cache:
            a1 = cache[key1]
            a2 = cache[key2]
            cache[key] = max(v[i]+a1, a2)
        elif key1 in cache:
            a1 = cache[key1]
            cache[key] = max(v[i]+a1, knap(i-1, _w))
        elif key2 in cache:
            a2 = cache[key2]
            cache[key] = max(v[i]+knap(i-1,_w-w[i]), a2)
        else:
            cache[key] = max(v[i]+knap(i-1,_w-w[i]), knap(i-1, _w))
    else:
        key2 = str(i-1)+"//-//"+str(_w)
        if key2 in cache:
            cache[key] = cache[key2]
        else:
            cache[key] = knap(i-1,_w)
            
    return cache[key]



knap(n-1,W)
print(cache[str(n-1)+"-"+str(W)])
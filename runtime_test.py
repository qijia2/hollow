"""
The runtime test measures the difference of three opeartions: insert, delete_min, and decerease_key
for Binary heap, these three Big O are: O(logn), O(logn), O(logn)
but for Holloew heap: they are O(1), O(logn), O(1)
The choosen binary heap is "heapq" standard library. The library is highly optimized, so the comparsion result
can not reach estimation.
"""
import time
import random
import heapq
from hollow import Hollow
random_seed = 100
random.seed(random_seed)

heap = Hollow()
keys = random.sample(range(-1000000, 1000000), 1000000)         # use random integers as key, value pair to insert
nodes = []
heapq_nodes = []
length = len(keys)
heapq.heapify(heapq_nodes)

print("\n.........Insertion time comparsion...........\n")        # measures the running time of insertion in standard binary heap, expected O(logn)

start = time.perf_counter()                                      # use time library to measure the running time
for i in range(length):
    heapq.heappush(heapq_nodes, keys[i])
end = time.perf_counter()
ms = (end-start) * 10**6
print(f"Binary insertion: Elapsed {ms:.03f} micro secs.")


start = time.perf_counter()
for i in range(length):                                      # measures the running time of insertion in hollow heap, expected O(1)
    nodes.append(heap.insert(keys[i]))
end = time.perf_counter()
ms = (end-start) * 10**6
print(f"Hollow insertion: Elapsed {ms:.03f} micro secs.")

print("\n................End comparsion.................\n")

print("\n.........delete_min time comparsion...........\n")

start = time.perf_counter()
for i in range(500000):
    heapq.heappop(heapq_nodes)                                
end = time.perf_counter()                                    # measures the running time of delete_min in standard binary heap, expected O(logn)
ms = (end-start) * 10**6
print(f"Binary delete_min: Elapsed {ms:.03f} micro secs.")


start = time.perf_counter()
for i in range(500000):
    heap.delete_min()                                        # measures the running time of delete_min in hollow heap, expected O(logn)
end = time.perf_counter()
ms = (end-start) * 10**6
print(f"Hollow delete_min: Elapsed {ms:.03f} micro secs.")

print("\n................End comparsion.................\n")


print("\n.........decrease_key time comparsion...........\n")

heap = Hollow()
keys = random.sample(range(-1000000, 1000000), 100000)
nodes = []
heapq_nodes = []

for k in keys:
    nodes.append(heap.insert(k))
    heapq_nodes.append(k)

length = len(keys)
heapq.heapify(heapq_nodes)

start = time.perf_counter()                                   
for _ in range(1000):                                      # measures the running time of decrease_key in standard binary heap, expected O(logn)

    index = random.randrange(len(nodes))
    key_new = heapq_nodes[index] - random.randint(1, 10000)            
    heapq.heappushpop(heapq_nodes, key_new)


end = time.perf_counter()
ms = (end-start) * 10**6
print(f"Binary decrease_key: Elapsed {ms:.03f} micro secs.")


start = time.perf_counter()
for _ in range(1000):                                     # measures the running time of decrease_key in hollow heap, expected O(logn)

    index = random.randrange(len(nodes))
    key_new = nodes[index].key - random.randint(1, 10000)

    nodes[index] = heap.decrease_key(nodes[index], key_new)

end = time.perf_counter()
ms = (end-start) * 10**6
print(f"Hollow decrease_key: Elapsed {ms:.03f} micro secs.")
print("\n................End comparsion.................\n")
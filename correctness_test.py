"""
The correctness_test program runs correctness tests for each individual function separately, and contains
a comprehensive correctness test as well. For each function, the program generates large number of keys to construct
the hollow heap, and check the correctness of the opeartion through the comparsion with doing exact same opeartion on
standard python list. If there is any mistake occur, the program will print "Failure" to indicate the hollow implementation is wrong.
If no "Failure" string is printed, it indicates the correctness of my hollow heap.
"""

import random
from hollow import Hollow
random_seed = 100
random.seed(random_seed)

# the function test the correctness of insert(), when only a single key is provided.
def insert_single_key_test():

    print("\n.........Do Insert Test..........")
    heap = Hollow()
    for k in [-1290, 0.1, 120, -1.111, 1.10019]:    # a list of single keys to insert

        n = heap.insert(k)
        if n.key != k or n.item.holding_value != k:    # if only one key is provided, item's value is set as its key
            print("Failure")
    print("............End Test..............\n")

# the function to test the correctness of insert(), when only a (key, value) pair is provided.
def insert_pair_test():

    print(".........Do Insert pair Test..........")
    heap = Hollow()
    for k, v in [(-10, 0), (0, "A"), (10, [1, 2]), (-1.1, {}), (1.1, 1.1)]:    # a list of pairs to insert

        n = heap.insert(k, v)
        if n.key != k or n.item.holding_value != v:
            print("Failure")
    print("............End Test..............\n")

# the function to test the correctness of find_min(), everytime compare the root of heap with the result of min() standard python function .
def find_min_test():

    print(".........Do Find_Min Test..........")
    heap = Hollow()
    keys = random.sample(range(-10000, 10000), 10000)    # use large amount of random numbers as keys, test find_min after every insertion
    added_keys = []
    for k in keys:

        added_keys.append(k)
        heap.insert(k)
        if heap.find_min().key != min(added_keys):    # print "Failure" when two methods return different min key
            print("Failure")

    print("............End Test..............\n")

# the function to test the correctness of delete_min, everytime compare the deleted root of hollow with the result of pop(0) standard python function .
def delete_min_test():

    print(".........Do Delete_Min Test..........")
    heap = Hollow()
    keys = random.sample(range(-10000, 10000), 100)

    for k in keys:
        heap.insert(k)
    keys = sorted(keys)     # sort the list in increasing order
    while len(keys) > 0:

        min_key = keys.pop(0)        # the min node of python list is popped
        heap_min = heap.delete_min()  
        if heap_min.key != min_key:    
            print("Failure")
    print("............End Test..............\n")

# the function to test the correctness of delete, after every deletion, check the min node to indicate correct deletion.
def delete_test():

    print(".........Do Delete Test..........")
    heap = Hollow()
    keys = random.sample(range(-10000, 10000), 10000)
    nodes = []
    for k in keys:
        nodes.append(heap.insert(k))
    
    while len(nodes) > 1:        # delete all nodes one by one
        node = nodes.pop(random.randrange(len(nodes)))
        heap.delete(node)
        if heap.find_min() != min(nodes, key=lambda n: n.key):    # check the min node after every deletion
            print("Failure")

    print("............End Test..............\n")

# the function to test the correctness of decrease_key, after every deletion, check the min node to indicate correct deletion.
def decrease_key_test():

    print(".........Do Decrease Key Test..........")
    heap = Hollow()
    keys = random.sample(range(-10000, 10000), 10000)
    nodes = []
    for k in keys:
        nodes.append(heap.insert(k))
    
    for _ in range(10000):

        index = random.randrange(len(nodes))                       # get the index of node to decrease key
        key_new = nodes[index].key - random.randint(1, 10000)         # get a random decreased new key
        nodes[index] = heap.decrease_key(nodes[index], key_new)

        if nodes[index].key != key_new:                               # ensure the key is decreased
            print("Failure")
        if heap.find_min() != min(nodes, key=lambda n: n.key):          # compare the min node
            print("Failure")

    print("............End Test..............\n")

# the function to test the correctness of meld, after every merge, check the min node to ensure correct merge.
def meld_test():

    print(".........Do Meld Test..........")
    heap = Hollow()
    heap.insert(1)
    all_keys = [1]
    for _ in range(10):                                        # perform 10 times of heap merge

        new_heap = Hollow()
        keys = random.sample(range(-1000, 1000), 100)          # construct a new heap in every iteration
        for k in keys:
            new_heap.insert(k)
        
        heap.meld(new_heap.h)
        all_keys.extend(keys)                                # extend the python list
        if heap.find_min().key != min(all_keys):             # compare the min node to ensure correctness of merge opeartion
            print("Failure")
    print("............End Test..............\n")

""" the function does a comprehensive test on the hollow heap implementation.
The test first insert (key, value) pair into the heap, both keys and values are randomly generated numbers.
Then it tests the delete function together with find_min function. Afterwards, the function tests merge by merging
with newly constructed heaps, then it tests decrease_key and delete_min. 
"""
def comprehensive_test():
    
    print("\n######### DO COMPREHENSIVE TEST ###########\n")
    heap = Hollow()
    keys = random.sample(range(-10000, 10000), 1000)        # insert random (key, value) pair into heap.
    vals = random.sample(range(-10000, 10000), 1000)
    nodes = []

    print("......doing insertion.....\n")
    for k in range(len(keys)):
        nodes.append(heap.insert(keys[k], vals[k]))

    print("......doing find min & delete.....\n")           
    while len(nodes) > 1:
        ind = random.randrange(len(nodes))
        node = nodes.pop(ind)                          # first delete a random node, then chek the correctness of min node by compare with python list function. 
        heap.delete(node)                 
        min_n = min(nodes, key=lambda n: n.key)
        
        if heap.find_min().key != min_n.key: print("Failure")
        if heap.find_min().item.holding_value != min_n.item.holding_value: print("Failure")

    print("......doing meld.....\n")
    for _ in range(10):
        new_heap = Hollow()
        new_keys = random.sample(range(-1000, 1000), 10)
        new_vals = random.sample(range(-1000, 1000), 10)
        
        for k in range(10):                                       
            nodes.append(new_heap.insert(new_keys[k], new_vals[k]))
        
        heap.meld(new_heap.h)                         # marge new heaps
        min_n = min(nodes, key=lambda n: n.key)
        
        if heap.find_min().key != min_n.key or heap.find_min().item.holding_value != min_n.item.holding_value:
            print("Failure")
    
    print("......doing decrease key test.....\n")
    for _ in range(1000):
        index = random.randrange(len(nodes))
        key_new = nodes[index].key - random.randint(1, 10000)
        nodes[index] = heap.decrease_key(nodes[index], key_new)
        min_n = min(nodes, key=lambda n: n.key)
        
        if nodes[index].key != key_new: print("Failure")                # test correctness by comparing keys and values
        if heap.find_min().key != min_n.key or heap.find_min().item.holding_value != min_n.item.holding_value: print("Failure")
    
    print("......doing delete min test.....\n")
    nodes = sorted(nodes)
    while len(nodes) > 0:

        min_n = nodes.pop(0)
        heap_min = heap.delete_min()              # every time delete min node, and compare with the result of pop(0) function in python list library.
        if heap_min.key != min_n.key:
            print("Failure")

    print("########### END COMPREHENSIVE TEST ###########\n")


if __name__ == "__main__":
    insert_single_key_test()
    insert_pair_test()
    find_min_test()
    delete_min_test()
    delete_test()
    decrease_key_test()
    meld_test()
    comprehensive_test()

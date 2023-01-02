"""
This program allows user to type and test their own data. The program
does not allow user to modify the key associated value. The program can test all operations except merge.
And since there is no much exceptional consideration in this file, please follow the printed instructions stractly.
Also, please remember the index of entering nodes, for example, the first entered node is index 0, the second entered node is index 1.
These indices will be used on delete and decrease_key opeartions.
"""
from hollow import Hollow
heap = Hollow()
heap_nodes = []


def insert_op():
    num = int(input("Please Enter the number of items you want to insert: \n"))

    print("if you want insert (key value) pair, please enter 1, if you only want insert key, enter 2: ")
    insert_type = int(input())
    for i in range(num):
        if insert_type == 1:
            k, v = input("Please Enter Your (key, value) pair, such as (2 pizza) separate by comma: \n").split(" ")
            k = int(k)
            heap_nodes.append(heap.insert(k, v))
        else:
            k = input("Please Enter Your key, such as (2): \n")
            k = int(k)
            heap_nodes.append(heap.insert(k))

def delete_op():
    print("please enter the index of node you want to delete: \n")
    ind = int(input())
    heap.delete(heap_nodes[ind])

def decrease_key_op():
    print("please enter the index of node you want to change: \n")
    ind = int(input())
    print("please enter the new key of node you want to change: \n")
    new_val = int(input())
    heap.decrease_key(heap_nodes[ind], new_val)


while True:
    print("Please Enter the opeartion you want to do: \n")
    print("1. insert, 2. delete, 3. delete_min, 4. decrease_key, 5. find_min, 6. exit")
    op = int(input())
    
    if op == 1:
        insert_op()
    elif op == 2:
        delete_op()
    elif op == 3:
        print((heap.delete_min()).key)
    elif op == 4:
        decrease_key_op()
    elif op == 5:
        print((heap.find_min()).key)
    elif op == 6:
        break
    else:
        print("wrong opeartion number. Retry")







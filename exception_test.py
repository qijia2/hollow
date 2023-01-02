"""
Some exception tests for my hollowheap.
"""
from hollow import Hollow

def meld_exception():
    ### A exception test for meld, indicates that the object to meld must be a node ###
    f1 = Hollow()
    f2 = Hollow()
    
    f1.insert(2)
    f1.insert(4)
    f2.insert(1)
    f2.insert(3)
    f2.insert(0)
    
    f1.meld(f2)     # here f2 is not a node, it is a heap, so it can not be merged      
    f1.meld(f2.h)      # now it becomes a node
    print((f1.find_min()).key == 0)      # "True" means merge succeeed.
    
    ### A exception test for meld, indicates merge with "none" type ###
    f1 = Hollow()
    f2 = Hollow()
    f1.insert(2)
    f1.insert(4)
    f1.meld(f2.h)                    # here, f2.h is "None", but the meld still works
    print((f1.find_min()).key == 2)     # "True" means merge succeeed.

    ### A exception test for meld, indicates "none" type merge with full node ###
    f1 = Hollow()
    f2 = Hollow()
    f2.insert(2)
    f2.insert(4)
    f1.meld(f2.h)                     # here, f2.h is node, but the f1's root is None, merge still works
    print((f1.find_min()).key == 2)

    ### A exception test for meld, indicates the merge two 'none type" yields "none"  ###
    f1 = Hollow()
    f2 = Hollow()
    f1.meld(f2.h)                   # empty heap merges with empty heap, still a None
    print(f1.h)

def decrease_key_exception():

    ### A exception test for decrease_key, indicates new key can not be larger than old one  ###
    f1 = Hollow()
    node = f1.insert(2)
    f1.insert(4)

    f1.decrease_key(node, 5)            # the new key is larger than old key, opearation fails

    f1.decrease_key(node, -1)            # now the opearation works
    print((f1.find_min()).key == -1)

    ### A exception test for decrease_key, indicates new key must be integer  ###
    f1 = Hollow()
    node = f1.insert(2)
    f1.decrease_key(node, "key")        # attempt to use string as a key, opeartion fails

def delete_exception():

    ### A exception test for delete_min, if there is nothing in the heap, you can not delete nothing  ###
    f1 = Hollow()
    f1.delete_min()

    ### A exception test for delete, if the node to be deleted is none, you can not delete nothing  ###
    node = f1.insert(2)
    f1.insert(8)
    f1.delete(None)                    # attempt to delete "none" type
    f1.delete(node)
    print((f1.find_min()).key == 8)

def insert_exception():

    ### A exception test for insert, the provided key must be numeric  ###
    f1 = Hollow()
    f1.insert("a", "aa")

    ### A exception test for insert, if the provided value is none, then set the key to be item's value   ###
    f1.insert(1)
    print((f1.find_min()).item.holding_value == 1)

if __name__ == "__main__":
    meld_exception()
    decrease_key_exception()
    delete_exception()
    insert_exception()
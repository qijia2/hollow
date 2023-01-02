"""
The below codes are my implementation of Hollow Heap, I defined three classes:
The Make_Item class constructs a item with attributes: node, holding_value
The Make_Node class constructs a node with attributes: item, child, next, ep, key, rank
as specified in the Hollow Heap paper.
The Hollow class constructs a hollow heap, the heap contains exactly same methods as specified in
the Hollow Heap paper, two-parent hollow heap.
The implementation of this file is exactly like pseducode on Hollow paper
Hollow Heap paper reference: 
https://arxiv.org/abs/1510.06535#:~:text=Hollow%20heaps%20combine%20two%20novel,the%20data%20structure%20its%20name.
"""

class Make_Item:

    def __init__(self, n, v):
        self.node = n
        self.holding_value = v

class Make_Node():

    def __init__(self, k, v):
        e = Make_Item(self, v)
        self.item = e
        self.child = None
        self.next = None
        self.ep = None
        self.key = k
        self.rank = 0
    
    def __lt__(self, another):
        if self.key < another.key:
            return True
        else:
            return False 

class Hollow():

    def __init__(self):
        self.h = None

    """ 
    The method is to insert a (key, value) pair, an "item" into the Hollow heap.
    IF the value is not provided,t the method will set the key as default value.
    """
    def insert(self, k, v=None):

        if not isinstance(k, int) and not isinstance(k, float):
            print("key must be numeric. Retry")
            return

        if v is None: v = k    # if the value is not provided, use key as its value
        bn = Make_Node(k, v)    # to construct the node to insert 
        self.h = self.meld(bn)    # use meld to link with existing root
        return bn
    
    """
    The method is to meld another node with roots of self heap, if the another node is
    root of another heap, then the method simply merges two heaps.
    """
    def meld(self, h):

        if self.h == None:
            self.h = h
            return h    # handle cases when one node is not provided
        if h == None: return self.h

        if not isinstance(h, Make_Node):    # the object to merge must be a node
            print("Only node can be merged. Retry.")
            return

        self.h = self.link(self.h, h)    # link two nodes
        return self.h
    
    """
    The method is to find the node with minimum item, it is just the root in hollow
    heap, then simply return the root node.
    """
    def find_min(self):

        h = self.h
        if h == None: return None
        else: return h
    
    """
    The method is to decrease a node u's key value to k, return the updated node for
    testing correctness(by compare with standard heap library).
    """
    def decrease_key(self, u, k):

        if not isinstance(k, int):
            print("The key must be integer. Retry")
            return

        if u.key < k:
            print("Error: the new key is larger than previous one")
            return

        # if the decrease happens on node pointing to minimum item, only change the key
        if u == self.h:
            u.key = k
            return self.h

        v = Make_Node(k, u.item.holding_value)    # construct a new node to replace the old one
        u.item = None    # make old node hollow

        # set old node the child of new node, update rank
        if u.rank > 2: v.rank = u.rank - 2
        v.child = u
        u.ep = v

        # update the root
        h = self.link(v, self.h)
        if h != self.h: self.h = h
        return v    # return the newly generated node for testing correctness of decrease_key()
    
    """
    The method delete the minimum node on the Hollow heap, it is the root in hollow.
    Return the deleted minimum node for testing correctness of delete_min() method(compare with standard heap).
    """
    def delete_min(self):

        prev = self.h
        self.h = self.delete(self.h)
        return prev
    
    """
    The link method links nodes accroding to the key value comparison,
    make the node with smaller key the parent of another.
    """
    def link(self, v, w):

        if v.key >= w.key:
            self.add_child(v, w)
            return w
        else:
            self.add_child(w, v)
            return v
    
    """
    The method simply set node v as node w's child.
    """
    def add_child(self, v, w):

        v.next = w.child
        w.child = v
    
    """
    The delete method delete a given item from hollow heap, make the corresponding
    node hollow, and if the node is the the root in heap, we repeatedly destroy hollow roots
    and link full roots until there are no hollow roots and at most one full root.
    """
    def delete(self, node):

        ## a exception: if node is None: return
        if not isinstance(node, Make_Node):
            print("you can only delete node. Retry")
            return

        node.item = None    # first step is to make the node hollow
        node = None

        # next, if the node to delete is not the root, then we done("lazy deletion")
        h = self.h        
        if self.h.item is not None: return self.h

        A = {}        # track all full roots
        max_rank = 0    # track the max rank
        h.next = None    # otherwise, h is the hollow root

        while h != None:

            w = h.child
            v = h
            h = h.next
            # execute for all children
            while w != None:

                u = w
                w = w.next
                # when u is hollow
                if u.item == None:

                    # case one: u is hollow and v is its only parent
                    if u.ep == None:
                        u.next = h
                        h = u
                    else:
                        # case two: u has two parents and v is the second
                        if u.ep == v: w = None
                        # case three: u has two parent and v is first
                        else: u.next = None
                        u.ep = None
                # when u is full
                else:
                    u, A, max_rank = self.do_ranked_links(u, A, max_rank)
        
        # finally, link all roots via unranked list until there is at most one
        self.h = self.do_unranked_links(h, A, max_rank)

        if self.h is not None: self.h.next = None
        #print("ddd_key: ", self.h.key, " ddd_val: ", self.h.item.holding_value)
        return self.h
    
    """
    The do_ranked_links method first Add u to A if two nodes share same rank. Then,
    link u with this root via a ranked link and repeat this with the winner until
    A does not contain a root of the same rank;  then add the final winner to A.
    """
    def do_ranked_links(self, u, A, max_rank):

        # add u to A when A has root of same rank, repeat until no same rank root in A
        while u.rank in A:

            # link u with corresponding root in A
            u = self.link(u, A[u.rank])
            del A[u.rank]
            u.rank += 1
        
        # add the final winner to A
        A[u.rank] = u
        if u.rank > max_rank:
            max_rank = u.rank
        return (u, A, max_rank)

    """
    The do_unranked_links links all roots via unranked list until there is at most one
    """
    def do_unranked_links(self, h, A, max_rank):

        # loop through all ranks
        for i in range(max_rank+1):

            if i in A and A[i] != None:

                if h == None: h = A[i]
                else: h = self.link(h, A[i])
                A[i] == None
        return h
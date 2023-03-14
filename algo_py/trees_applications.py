# -*- coding: utf-8 -*-
"""
2023-01
S3# - trees applications
"""

from algo_py import tree, treeasbin
from algo_py import queue

'''
3.1 tree -> list representation
return the linear representation of a tree 
"(r A0 A1 A2...)"
also in algopy/tree|treeasbin.py
'''

# to_linear(T: Tree): str
def to_linear(T):
    s = '(' + str(T.key)
    for child in T.children:
        s += to_linear(child)
    s += ')'
    return s

# to_linear_TAB(B: TreeAsBin): str
def to_linear_TAB(B):
    s = '(' + str(B.key)
    C = B.child
    while C != None:
        s += to_linear_TAB(C)
        C = C.sibling
    s += ')'
    return s
    


"""
3.2 tree -> dot
simple versions here
see in algopy/tree|treeasbin.py for the versions who work with duplicate keys
"""

# warning: the following versions do not work if keys are not unique 
# see algopy/tree.py for a version that uses id

def dot(T):
    """Write down dot format of tree.

    Args:
        T (Tree).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:
            s = s + "   " + str(T.key) + " -- " + str(child.key) + "\n"
            q.enqueue(child)
    s += "}"
    return s

def dotBin(B):
    """Write down dot format of tree.

    Args:
        B (TreeAsBin).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(B)
    while not q.isempty():
        B = q.dequeue()
        C = B.child
        while C:
            s = s + "   " + str(B.key) + " -- " + str(C.key) + "\n"
            q.enqueue(C)
            C = C.sibling
    s += "}"
    return s


"""
3.3 : Large Family
morechildren(B:TreeAsBin): bool test whether all internal nodes have more children 
than their parent in B
"""
# v1
def morechildren(B, nbc=0):
    """
    nbc is B's parent child number
    """
    k = 0
    C = B.child
    while C:
        k += 1
        C = C.sibling
    if B.child != None and k <= nbc:
        return False
    else:
        C = B.child
        while C and morechildren(C, k):
            C = C.sibling
        return C == None
        
# v2
def __nbchildren(T):
    """
    compute T's child number
    """
    k = 0
    C = T.child
    while C:
        k += 1
        C = C.sibling
    return k

def morechildren2(B, nbc=0):
    if B.child == None:
        return True
    else:
        k = __nbchildren(B)
        if k <= nbc:
            return False
        else:
            C = B.child
            while C != None:
                if not morechildren2(C, k):
                    return False
                C = C.sibling
            return True

# going up
def __more(B):
    """
    return B's number of children 
    or -1 if the property is False...
    """
    nbc = __nbchildren(B)
    C = B.child
    while C and nbc >= 0:
        nb_childC = __more(C)
        if nb_childC > 0 and nb_childC <= nbc:
            nbc = -1
        C = C.sibling
    return nbc
    

def __more2(B):
    """
    return B's number of children 
    or -1 if the property is False...
    """
    nbc = 0 # B's child number
    min_nb_childC = float('inf') # infinity
    C = B.child
    while C:
        nb_childC = __more2(C)
        if nb_childC == -1:
            return -1
        if nb_childC > 0:
            min_nb_childC = min(min_nb_childC, nb_childC)
        nbc += 1
        C = C.sibling
    if min_nb_childC <= nbc:
        return -1
    else:
        return nbc

def morechildren_up(B):
    return __more(B) > 0
    
'''
3.4: External Average Depth: 
sum of leaf depths divided by the number of leaves
Can be done with a simple BFS, here with a DFS
'''

# with "classical" implem
def __count(T, depth=0):
    """
    T: Tree
    depth: actual depth
    returns (sum of leaf depths, nb leaves)
    """
    if T.children == []:
        return (depth, 1)
    else:
        (sum_depths, nb_leaves) = (0, 0)
        for child in T.children:
             (s, n) = __count(child, depth+1)
             sum_depths += s
             nb_leaves += n
        return (sum_depths, nb_leaves)
    
        
def external_average_depth(T):
    (sum_depths, nb_leaves) = __count(T)
    return sum_depths / nb_leaves

    
# with TreeAsBin
def __count_tab(B, depth=0):
    """
    B: TreeAsBin
    depth: actual depth
    returns (sum of leaf depths, nb leaves)
    """    
    if B.child == None:
        return (depth, 1)
    else:
        Bchild = B.child
        (sum_depths, nb_leaves) = (0, 0)
        while Bchild != None:
            (s, n) = __count_tab(Bchild, depth+1)
            sum_depths += s
            nb_leaves += n
            Bchild = Bchild.sibling
    return (sum_depths, nb_leaves)
        

def external_average_depth_TAB(B):
    (sum_depths, nb_leaves) = __count_tab(B)
    return sum_depths / nb_leaves
 

"""
Extra: equality Tree & TreeAsBin
"""

# with return in loop
def same(T, B):
    if T.key != B.key:
        return False
    else:
        Bchild = B.child
        for Tchild in T.children:
            if Bchild == None or not(same(Tchild, Bchild)):
                return False
            Bchild = Bchild.sibling
    return Bchild == None

def same2(T, B):
    if B.key != T.key:
        return False
    i = 0
    C = B.child
    while i < T.nbchildren and C != None:
        if not same2(T.children[i], C):
            return False
        i += 1
        C = C.sibling
    return C == None and i == T.nbchildren

# without return in the loop
def same3(T, B):
    if T.key != B.key:
         return False
    else:
         Bchild = B.child
         i = 0
         while i < T.nbChildren and Bchild and \
                         same3(T.children[i], Bchild):
             i += 1
             Bchild = Bchild.sibling
         return i == T.nbChildren and Bchild == None


"""
3.6-1
treeasbin_to_tree(B: TreeAsBin): Tree 
return a copy of B, implemented in first child - right sibling in "classical" implementation
"""

def treeasbin_to_tree(B):
    T = tree.Tree(B.key, [])
    child = B.child
    while child != None:
        T.children.append(treeasbin_to_tree(child))
        child = child.sibling
    return T


    
"""
3.6-2
tree_to_treeasbin(T: Tree): TreeAsBin
convert T from  "classical" implementation to first child - right sibling  (return a copy of T)
"""

# with "insertions" at the end
def tree_to_treeasbin_(T):
    B = treeasbin.TreeAsBin(T.key, None, None)
    if T.nbchildren != 0:
        B.child = tree_to_treeasbin(T.children[0])
        last = B.child
        for i in range(1, T.nbchildren):    
            last.sibling = tree_to_treeasbin_(T.children[i])
            last = last.sibling
    return B





# "insertions at the head"
def tree_to_treeasbin(T):
    B = treeasbin.TreeAsBin(T.key, None, None)
    firstchild = None
    for i in range(T.nbchildren-1, -1, -1):
        C = tree_to_treeasbin(T.children[i])
        C.sibling = firstchild
        firstchild = C
    
    B.child = firstchild
    return B



"""
3.7 Bonus
"linear representation" -> Tree (int keys)
The string is assumed correct!
also in algopy/tree.py
"""

def __from_linear(s, i=0): 
        i += 1 # to skip the '('
        key = ""
        while s[i] != '(' and s[i] != ')':  # s[i] not in "()"
            key += s[i]
            i += 1
        T = tree.Tree(int(key), [])
        while s[i] != ')':  # s[i] == '('
            (C, i) = __from_linear(s, i)
            T.children.append(C)
        i += 1 # to skip the ')'
        return (T, i)

def from_linear(s):
    (T, _) = __from_linear(s)
    return T



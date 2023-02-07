__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixtrees.py 2023-02-03'

"""
Prefix Trees homework
2023-02 - S3#
@author: antoine.leveque
"""

from algo_py import ptree

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

##############################################################################
## Measure
 
import prefixtreesexample
test = prefixtreesexample.Tree1

def count_words(T): # fonctionne
    """ count words in the prefix tree T (ptree.Tree)
    return type: int
    """
    res = 0
    if T.key[1]==True:
        res+=1
    for child in T.children:
        res+=count_words(child)
    return res

def longest_word_length_inter(T,height): # à documenter
    """
    Auxiliary function
    T : a prefix tree T (ptree.Tree)
    height : the initial height (int)
    return the lenght of the longest word in the first T tree at the height height
    return type : int
    """
    if T.nbchildren==0:
        return height
    L = []
    for child in T.children:
        L.append(longest_word_length_inter(child,height+1))
    return max(L)

def longest_word_length(T):
    """ longest word length in the prefix tree T (ptree.Tree)
    return type: int    
    """
    return longest_word_length_inter(T,0)

def count_height(T,height,res):
    """
    Auxiliary function
    T : a prefix tree T (ptree.Tree)
    height : the initial height (int)
    res : the result (int)
    return the result of the sum of all the words's height in the T tree
    return type : int
    """
    if T.key[1]==True:
        res+=height
    for child in T.children:
        res = count_height(child,height+1,res)
    return res

def average_length(T):
    """ average word length in the prefix tree T (ptree.Tree)
    return type: float
    """
    return count_height(T,0,0)/count_words(T)
    
###############################################################################
## search and list

def word_list(T):
    """ generate the word list of the prefix tree T (ptree.Tree)
    return type: str list
    """
    #FIXME
    pass
        

def contains(L,x):
    """
    Auxiliary function
    L : a list of children ((char,bool))
    x : a character (string)
    Check if the element x is in the list L. Return also the index of the element in L, L lenght otherwise
    return type (bool,int)
    """
    state = False
    i=0
    while i<len(L) and state==False:
        state = (L[i]).key[0]==x
        i+=1
    return (i!=len(L),i)

def search_word(T, w): # fonctionne
    """ search for the word w (str) not empty in the prefix tree T (ptree.Tree)
    return type: bool
    """
    state = True
    i = 0
    C = T
    max = len(w)
    while C.nbchildren!=0 and state and i<max:
        temp = contains(C.children,w[i])
        if temp==(False,C.nbchildren):
            state = False
        else:
            i+=1
            index = temp[1]
            C = C.children[index]
    return state and C.key[1]==True and i == max
    
def completion(T, prefix):
    """ generate the list of words in the prefix tree T (ptree.Tree) with a common prefix 
    return type: str list    
    """
    s = ""
    i = 0
    C = T
    state = True
    while s!=prefix and state: # recherche de l'arbre contenant tous les mots avec comme préfixe prefix
        temp = contains(C.children,prefix[i])
        if temp==(False,C.nbchildren):
            state = False
        else:
            s+=prefix[i]
            i+=1
            index = temp[1]
            C = C.children[index]
    return word_list(C)

###############################################################################
## Build

def build_lexicon(T, filename):
    """ save the tree T (ptree.Tree) in the new file filename (str)
    """
    
    #FIXME
    pass


def add_word(T, w): # fonctionne
    """ add the word w (str) not empty in the tree T (ptree.Tree)
    """
    i = 0
    C = T
    while i<len(w) and contains(C.children,w[i])!=(False,C.nbchildren):
        temp = contains(C.children,w[i])
        i+=1
        index = temp[1]
        C = C.children[index]
    while i<len(w):
        (C.children).append(ptree.Tree((w[i],i==len(w)-1),None))
        i+=1
        C = C.children[C.nbchildren-1]

def build_tree(filename):
    """ build the prefix tree from the file of words filename (str)
    return type: ptree.Tree
    """
    T = ptree.Tree(("",False),None)
    file = open(filename,'r')
    for each in file:
        add_word(T,each)
    file.close
    return T

def same(T1,T2):
    if T1.key!=T2.key or T1.nbchildren!=T2.nbchildren:
        return False
    else:
        state = True
        i = 0
        while i < T1.nbchildren:
            state = same((T1.children)[i],(T2.children)[i])
            i += 1
        return state
test2 = build_tree("lexicons/wordList1.txt")
print(count_words(test2))
 #print(same(test,build_tree("lexicons/wordList1.txt")))
__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixtrees.py 2023-02-03'

"""
Prefix Trees homework
2023-02 - S3#
@author: login
"""

from algo_py import ptree

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

##############################################################################
## Measure

def count_words(T):
    """ count words in the prefix tree T (ptree.Tree)
    return type: int
    """
    
    #FIXME
    pass
    

def longest_word_length(T):
    """ longest word length in the prefix tree T (ptree.Tree)
    return type: int    
    """
    
    #FIXME
    pass


def average_length(T):
    """ average word length in the prefix tree T (ptree.Tree)
    return type: float
    """
    
    #FIXME
    pass
    
###############################################################################
## search and list

def word_list(T):
    """ generate the word list of the prefix tree T (ptree.Tree)
    return type: str list
    """
    
    #FIXME
    pass


def search_word(T, w):
    """ search for the word w (str) not empty in the prefix tree T (ptree.Tree)
    return type: bool
    """
    
    #FIXME
    pass
    
    
def completion(T, prefix):
    """ generate the list of words in the prefix tree T (ptree.Tree) with a common prefix 
    return type: str list    
    """
    
    #FIXME
    pass


###############################################################################
## Build

def build_lexicon(T, filename):
    """ save the tree T (ptree.Tree) in the new file filename (str)
    """
    
    #FIXME
    pass


def add_word(T, w):
    """ add the word w (str) not empty in the tree T (ptree.Tree)
    """
    
    #FIXME
    pass


def build_tree(filename):
    """ build the prefix tree from the file of words filename (str)
    return type: ptree.Tree
    """
    
    #FIXME
    pass   

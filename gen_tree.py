"""
Arbres généraux :
    - A = <r,liste d'arbres>
    - A = <r,{A0,...,An}>
    - T : l'arbre T
    - T.key = valeur de la clé
    - T.children : liste des sous-arbres
    - T.nbchildren : nombre de fils du noeud T

- lien dans git bash : cd OneDrive\ -\ EPITA/Algorithmique/S3/

    - B : TreeAsBin
    - B.key : valeur de la clé
    - B.child : lien vers le premier fils gauche
    - B.sibling : lien vers le premier frère droit
    - noeud est une feuille quand B.child == None
"""

from algopy import tree
from algopy import treeasbin

# Partie 1 : Mesures

# Ex 1.1 : La taille
def size(T):    # arbre général
    n = 1
    #pour chaque sous-arbre de Ai (sera le cas d'arrêt si le noeud est une feuille)
    #   n+=size(Ai)
    for c in T.children:
        n+=size(c)
    return n

def sizebin(B):    # bijection fils frère-droit
    n = 1
    # instructions
    C = B.child
    while(C!=None):
        n+=sizebin(C)
        C = C.sibling
    return n

def getMax(L):
    max = L[0]
    for elt in L:
        if(elt>max):
            max = elt
    return max

"""
La hauteur d'un arbre est le nombre de lien entre la racine de l'arbre et la feuille la plus éloignée de la racine de l'arbre
"""

def height(T,n=0):  # arbre général
    if(T.nbchildren!=0):    # si l'arbre n'est pas une feuille
        L=[]    # on crée une liste
        for c in T.children:
            L.append(height(c,n+1)) # dans laquelle on met la profondeur de tous ses fils
        n = getMax(L)   # on ne garde que la valeur maximale de la liste
    return n # on retourne la hauteur du noeud

def heightbin(B,n=0):
    C = B.child # on prend son premiers fils
    L = [n] # on crée une liste avec la valeur de la hauteur actuelle
    while(C.sibling!=None): # pour tous les frères du premier fils du noeud initial
        L.append(heightbin(C.child,n+1))   # on ajoute à la liste leur hauteur
    return getMax(L)    # on retourne la valeur maximale

def heightbin2(B):
    if B==None:
        return -1
    else:
        return max(1 + heightbin2(B.child),heightbin2(B.sibling))
    
# Partie 2 : Parcours

# Ex 2.1 : Parcours profondeur   
def DFStree(T): # arbre général
    s = '<' + str(T.key)
    if T.nbchildren!=0:
        for i in range(T.nbchildren-1):
            DFStree(T.children[i])
            s+=','
        DFStree(T.children[-1])
    s+='>'
    print(s)

def DFSbin(B):  # arbre bijection premier fils-frère droit
    s='<'+str(B.key)
    if B.child!=None:
        C = B.child
        while C.sibling!=None:
            DFSbin(C)
            s+=','
            C = C.sibling
        DFSbin(C)
    s+='>'
    print(s,end='')

# Ex 2.2 : Parcours largeur


# Partie 3 : Applications

# Ex 3.1 : Représentation linéaire
def to_linear_tree(T):
    s = "("+T.key
    for c in T.children:
        s+=to_linear_tree(c)
    s+=")"
    return s

def to_linear_bin(B):
    s = "(" + B.key
    C = B.child
    if C.child!=None:
        s+=to_linear_bin(C) + ")"
    if C.sibling!=None:
        s+=to_linear_bin(C.sibling)
    s+=")"
    return s
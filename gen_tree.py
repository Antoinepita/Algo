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

def height(B,n=0):
    C = B.child # on prend son premiers fils
    L = [n] # on crée une liste avec la valeur de la hauteur actuelle
    while(C.sibling!=None): # pour tous les frères du premier fils du noeud initial
        L.append(height(C.child,n+1))   # on ajoute à la liste leur hauteur
    return getMax(L)    # on retourne la valeur maximale
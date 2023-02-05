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
from algopy import queue

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
"""
Pseudo algo : méthode avec une pile et marqueur de changement de niveau
    f = file.vide()
    enfiler(f,racine)
    enfiler(f,/)
    tant que f != vide
        N = defiler(f)
        si N = / :
            si f != vide :
                enfiler(f,/)
            fin si
        sinon
            pour chaque fils Fi de N
                enfiler(f,Fi)
            fin pour
            # enfiler(f,/) # si on met cette instruction là, ça va poser pb à partir du 2eme niveau
        fin si
    fin tant que

    
Pseudo algo : méthode avec deux files

"""
def BFS(T):     # arbre général avec méthode une pile + marqueur de niveau
    q = queue.Queue()
    q.enqueue(T)
    q.enqueue(None)
    while not q.isempty():
        N = q.dequeue()
        if N==None:
            print()
            if not q.isempty():
                q.enqueue(None)
        else:
            print(T.key, end=' ')
            for children in T.children:
                q.enqueue(children)


def BFS_TAB_2(B):     # arbre bijection premier fils-frère droit avec méthode double pile
    q_out = queue.Queue()
    q_in = queue.Queue()
    q_out.enqueue(B)
    while not q_out.isempty():
        B = q_out.dequeue()
        print(B.key, end=' ')
        C = C.child
        while C != None:
            q_in.enqueue(C)
            C = C.sibling
        if q_out.isempty():
            print()
            q_out = q_in
            q_in = queue.Queue()


# Partie 3 : Applications

# Ex 3.1 : Représentation linéaire
def to_linear_tree(T):
    s = "("+ str(T.key)
    for c in T.children:
        s+=to_linear_tree(c)
    s+=")"
    return s

def to_linear_bin(B):
    s = "(" + str(B.key)
    C = B.child
    if C.child!=None:
        s+=to_linear_bin(C)
    s += ")"
    if C.sibling!=None:
        s+=to_linear_bin(C.sibling)  
    # s += ")"      # exemple du noeud racine : n'a pas de frère
    return s

def to_linear_TAB(B):   # correction prof
    s = "(" + str(B.key)
    C = B.child
    while C != None:
        s+=to_linear_TAB(C)
        C = C.sibling
    s+=")"
    return s

# Ex 3.2 : format dot
def toDot(T):       # arbre général
    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:
            s += str(T.key) + " -- " + str(child.key) + "\n"
    s+="}"
    return s

def toDot_TAB(B):   # arbre binaire
    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:    # il faut modifier cette ligne là
            s += str(T.key) + " -- " + str(child.key) + "\n"
    s+="}"
    return s

def morechildren(T,n=0):
    if T.children==0:
        return True
    if T.nbchildren<=n:
        return False
    else:
        for child in T.children:
            if not morechildren(child,T.nbchildren):
                return False
        return True
    
def morechildren_TAB(B, n = 0):    # arbre bijection premier fils-frère droit
    if B.child==None:
        return True
    C = B.child
    nbchildren = 1
    while C.sibling:
        nbchildren+=1
        C = C.sibling
    if nbchildren<=n:
        return False
    else:
        while C and morechildren(C, nbchildren):
            C = C.sibling
        return C==None
    
# Ex 3.4 : PME

def nb_height(T,nb,height):
    if T.nbchildren==0:
        return (nb+1,height)
    else:
        (number,hauteur)=(0,0)
        for child in T.children:
            couple = nb_height(child,nb,height+1)
            number += couple[0]
            hauteur += couple[1]
        return (number,hauteur)

def pme(T):
    couple = nb_height(T,0,0)
    return couple[1]/couple[0]

def nb_height_TAB(B,nb,height):
    if B.child==None:
        return (nb+1,height)
    else:
        C = B.child
        (number,hauteur)=(0,0)
        while C:
            couple = nb_height_TAB(C,nb,height+1)
            number += couple[0]
            hauteur += couple[1]
            C = C.sibling
        return(number,hauteur)

def pme(B):
    couple = nb_height_TAB(B,0,0)
    return couple[1]/couple[0]
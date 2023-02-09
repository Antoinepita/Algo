#from algo_py import  btree

"""
Arbres-B :
    - classe B:BTree
        - B.keys : liste de clés
        - B.children : liste des sous-arbres
        - B.nbkeys : nombre de fils (= len(B.nbkeys))
        - B.degree : degré de l'arbre
    
"""

# Partie 1 : Préliminaires

"""
Ex 1.1 :
    1) Arbre général de recherche :
        - k.noeuds = k-1 clés
                     k fils si k est un noeud interne
        - x0 < x1 < ... < xi < x(i+1) < ... < x(k-2)

    2) Arbre B (de degré/d'ordre T):
        - arbre général de recherche
        - feuilles toutes au même niveau
        - t <= k <= 2t sauf racine 2<=k<=2t

    3) 
    
"""

# Ex 1.3 : Liste des éléments en ordre croissant d'un arbre
def _build(B,L):
    if B.children==[]:  # cas feuille
        for elt in B.keys:
            L.append(B.keys[i])
    else:
        for i in range(B.nbkeys):   # len(B.children)-1
            _build(B.children[i],L)
            L.append(B.keys[i])
        _build(B.children[B.nbkey],L)   # B.children[-1]
            

def btree2list(B):
    L = []
    _build(B,L)
    return L

# Partie 2 : Classiques

"""
Ex 2.1 : Minimum et maximum
1) La valeur minimale correspond à la première clé de la feuille la plus à gauche et la valeur maximale est la dernière clé de la feuille la plus à droite
"""

def getMin(B):
    C = B
    while C.nbkeys!=0:  # bord gauche
        C = C.children[0]
    return C.keys[0]    # valeur de la première clé

def getMax(B):
    C = B
    while C.nbkeys!=0:  # bord droit
        C = C.children[-1]
    return C.keys[-1]   # valeur de la dernière clé

# Ex 2.2: Recherche d'un élément
def dicho(L,x):
    """
    renvoie la place de l'élément x dans la liste triée en ordre croissant L
    renvoie l'index juste avant lequel il devrait être inséré s'il n'y est pas
    """
    a = 0
    b = len(L)-1
    m = (a+b)//2
    while a < b :
        if L[m] ==  x:
            return m
        elif L[m] > x:
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a

print(dicho([0,1,2,3,4,5,6,7,8,9],))

def search(B,x):
    i = dicho(B.keys,x)
    if B.keys[i]==x:    # cas d'arrêt : valeur trouvée
        return (B,i)
    if B.keys[i]!=x and (B.keys[i]).children==0:    # cas d'arrêt : valeur pas trouvée dans la liste et pas d'enfant donc n'est pas dans l'arbre
        return None
    else:
        if x>B.keys[i]: # sinon on réeffectue la recherche sur :
            search(B.children[i+1],x) # le sous arbre droit de là où il devrait se trouver si x>clé actuelle 
        else:
            search(B.children[i],x) # le sous-arbre gauche sinon (x<=valeur de la clé actuelle)

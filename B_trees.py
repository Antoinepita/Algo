from algo_py import btree

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
    while B.children!=[]:  # bord gauche
        B = B.children[0]
    return B.keys[0]    # valeur de la première clé

def getMax(B):
    while B.children!=[]:  # bord droit
        B = B.children[-1]
    return B.keys[-1]   # valeur de la dernière clé

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

def search(B,x):
    i = dicho(B.keys,x)
    if i<B.nbkeys and B.keys[i]==x:    # cas d'arrêt : valeur trouvée   / erreur commune : oubli de la première cdt : si l'index dépasse
        return (B,i)
    if B.children==[]:  # cas d'arrêt : cas feuille et valeur pas trouvée
        return None
    else:
        return search(B.children[i],x)

"""
Ex 2.3 : Insertion d'un élément (méthode classique)
B-arbre de degré t:
    - k.noeuds : t<=k<=2t
        --> sauf racine : 2<=k<=2t
    - toutes les feuilles sont au même niveau
    - si le noeud n'est pas plein : on ajoute à l'index nécessaire
    - sinon :
        - (pas compris)    
"""

def split(B,i):
    mid = B.degree-1
    L = B.children[i]
    R = btree.BTree()
    # keys
    (L.keys,x,R.keys) = (L.keys[:mid],L.keys[mid],L.keys[mid+1])
    # children
    if L.children!=[]:
        (L.children,R.children) = (L.children[:mid+1],L.children[mid+1:])
    # root
    B.keys.insert(i,x)
    B.children.insert(i+1,R)
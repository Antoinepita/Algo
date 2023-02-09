from algo_py import  btree

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
        for i in range(len(B.keys)):
            L.append(B.keys[i])
    else:
        for i in range(B.nbkeys):   # len(B.children)-1
            _build(B.children[i],L)
        _build(B.children[B.nbkey],L)   # B.children[-1]
            

def btree2list(B):
    L = []
    _build(B,L)
    return L
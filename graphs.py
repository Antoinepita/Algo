"""
Les graphes :
    - noté G = <S,A>
    - ordre du graphe = |S|
    - p = |A|

    
Classe GraphMat : (matrices d'adjacences)
    - G.adj[i][j] = nombre de liens entre le sommet i et j
    - pour créer un graphe : 
        - [nom du graphe] = graphmat.GraphMat([ordre du graphe],[graphe orienté ?])
        - [nom du graphe].adj = [la matrice d'adjacences qu'on veut]

Classe Graph : (listes d'adjacences)
    - pour créer un graphe : 
        - [nom du graphe] = graph.Graph([ordre du graphe],[graphe orienté ?])
        - [nom du graphe].adjlists = [les listes d'adjacences qu'on veut]
"""
from algo_py import graphmat, graph
import ex_graphs as examp

graphmat1 = examp.G1mat
graph1 = examp.G1
graphmat2 = examp.G2mat
graph2 = examp.G2

# Ex 1.3 : Degré d'un graph

def degrees(graph):
    L = [0] * graph.order # initialisation d'une liste de 10 éléments à 0
    for i in range(graph.order):
        for j in range(graph.order):
            L[i] += graph.adj[i][j]
            if(i==j):
                L[i] += 1
    return L

#print(degrees(graphmat1))

def in_out_degrees(graph):
    inte = [0] * graph.order
    out = [0] * graph.order
    for i in range(graph.order):
        for j in graph.adjlists[i]:
            out[i]+=1 # demi-degré extérieur
            inte[j] += 1 # demi-degré intérieur
    return (inte,out)

# print(in_out_degrees(graph1))

def outdegree(graph):
    return [len(L) for L in graph.adjlists]
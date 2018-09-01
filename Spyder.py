import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
def ldata(archive):
    f=open(archive)
    data=[]
    for line in f:
        line=line.strip()
        col=line.split()
        data.append(col)
    return data

red_proteinas=ldata("data/yeast_AP-MS.txt")
red_binarias=ldata("data/yeast_Y2H.txt")
red_literatura=ldata("data/yeast_LIT.txt")
red_prueba=ldata("data/prueba.txt")

G = nx.Graph()#directed
G.add_edges_from(red_proteinas)
nx.draw(G, with_labels=False, font_weight='bold',node_size=2)
plt.title("Red proteinas")
plt.show()
G.number_of_nodes()

G1 = nx.DiGraph()#directed
G1.add_edges_from(red_binarias)
nx.draw(G1, with_labels=False, font_weight='bold',node_size=2)
plt.title("Red binarias")
plt.show()
G1.number_of_nodes()

G2 = nx.DiGraph()#directed
G2.add_edges_from(red_literatura)
nx.draw(G2, with_labels=False, font_weight='bold',node_size=2)
plt.title("Red literatura")
plt.show()
G2.number_of_nodes()

red_literatura_trans=[]
for j in red_literatura:
    red_literatura_trans.append([j[1],j[0]])
a_red_literatura=0
for j in red_literatura_trans:
    for i in red_literatura:
        if i==j:
            a_red_literatura+=1
print(a_red_literatura)

red_proteinas_trans=[]
for j in red_proteinas:
    red_proteinas_trans.append([j[1],j[0]])
a_red_proteinas=0
for j in red_proteinas_trans:
    for i in red_proteinas:
        if i==j:
            a_red_proteinas+=1
print(a_red_proteinas)

red_binarias_trans=[]
for j in red_binarias:
    red_binarias_trans.append([j[1],j[0]])
a_red_binarias=0
for j in red_binarias_trans:
    for i in red_binarias:
        if i==j:
            a_red_binarias+=1
print(a_red_binarias)

def K(H,a_R):
    if a_R >0:
        k_in=sum(H.in_degree(k) for k in H)/H.number_of_nodes()
        k_out=sum(H.out_degree(k) for k in H)/H.number_of_nodes()
        salida=[k_in,k_out]
    else:
        k=sum(H.degree(k) for k in H)/H.number_of_nodes()
        salida=[k]
    return salida

K(G,a_red_proteinas)
K(G1,a_red_binarias)
K(G2,a_red_literatura)

def Min(H,a_R):
    if a_R >0:
        M=min(H.in_degree(k) for k in H )
        Mbis=min(H.out_degree(k) for k in H )
        MINIMO=[M,Mbis]
        
    else:
        Mini=min(H.degree(k) for k in H)
        MINIMO=[Mini]
    return MINIMO

def Max(H, a_R):
    if a_R >0:
        Ma=max(H.in_degree(k) for k in H)
        Mabis=max(H.out_degree(k) for k in H)
        MAXIMO=[Ma, Mabis]
    else:
        Maxi=max(H.degree(k) for k in H)
        MAXIMO=[Maxi]
    return MAXIMO

data = pd.DataFrame({"Red":["Proteinas","Binarias","Literatura"],"Nodos":[G.number_of_nodes(),G1.number_of_nodes(),G2.number_of_nodes()],
                     "Enlaces":[G.number_of_edges(),G1.number_of_edges(),G2.number_of_edges()],
                     "Dirigida":["No","Sí","Sí"],"Grado medio ([in, out])":[K(G,a_red_proteinas),K(G1,a_red_binarias),K(G2,a_red_literatura)],"Grado máximo([in,out])":[Max(G,a_red_proteinas),Max(G1,a_red_binarias),Max(G2,a_red_literatura)],"Grado mínimo([in,out])":[Min(G,a_red_proteinas),Min(G1,a_red_binarias),Min(G2,a_red_literatura)]})
data
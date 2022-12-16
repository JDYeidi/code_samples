#Algoritmo A* 

#Importación de librerías
from asyncio.windows_events import NULL
import pandas as pd

#Leemos el dataframe
df_edges = pd.read_csv("edges.csv", header=None)
df_nodes = pd.read_csv("nodes.csv", header=None)

#Obtenemos los nodos del data frame
nodos = df_nodes.iloc[:,0:1]
#Ajustamos la dimensión del array para convertirlo en 1D
nodos = nodos.to_numpy().flatten()
#Obtenemos la distancia Heuristica de cada nodo
Heuristic = df_nodes.iloc[:,3]
Heuristic = Heuristic.to_numpy()
#print(Heuristic[1])
#Obtenemos las parejas de vecinos con su costo del data frame edges
#Matriz 3 columnas con 19 filas
# D1 | D2 | Costo #
vecinos = df_edges.iloc[:,0:]
vecinos = vecinos.to_numpy()

#Organizamos los datos obtenidos en un diccionario para acceder a ellos de forma más sencilla
#Diccionario general del grafo
grafo = {}
heuristic = {}
#Diccionario que guardara los vecinos de cada nodo con su costo
nbr_dic = {}
contador = 0

#Declaramos las variables g,f score
g_score = 0
f_score = 1
previous = 2

#Pimera vuelta
PV = True

#Creación del grafo principal
for nodo_actual in nodos:
    for nbrs in vecinos:
        if nodo_actual in nbrs and nbrs[0] == nodo_actual:
            nbr_dic[nbrs[1]] = nbrs[2] 
        elif nodo_actual in nbrs and nbrs[1] == nodo_actual:
            nbr_dic[nbrs[0]] = nbrs[2]
        else:
            continue
    grafo[nodo_actual] = nbr_dic
    nbr_dic = {}
#Diccionario con los costos heurísticos
for i in nodos:
    heuristic[i] = Heuristic[i-1]

#Funcion que obtiene el nodo con el mínimo fscore
def min_fscore(unvisited_nodes, nbr, parents):
    
    lst = []
    keys = []
    
    for key in unvisited_nodes:
        print(unvisited_nodes[key][1],key)
        keys.append([unvisited_nodes[key][1],key])
        lst.append(unvisited_nodes[key][1])

    minm = min(lst)
    for i in keys:
        if i[0] == minm:
            print(i[1])
            return i[1], minm
                    


print(grafo)

def A_star(grafo, start_node=1, target_node = 8):

    #Lista de nodos visitados vacía
    visited_nodes = {}
    #Lista de nodos no visitados vacía
    unvisited_nodes = {}

    parents = []

    #Agregamos los Nodos a la lista de no visitados
    #LLave(Nodo), g-score, f-score, nodo previo
    #             Infinito,infinito,
    for key in grafo:
        unvisited_nodes[key] = [1000000, 1000000, NULL]

    #Actualizamos los valores del nodo inicial en la lista de los NO VISITADOS
    heuristic_score =heuristic[start_node]
    #LLave(Nodo), g-score, f-score, nodo previo
    unvisited_nodes[start_node] = [0, heuristic_score, NULL]
    
    #Bandera para saber si llegamos a la meta
    finish = False
    current_node  = start_node

    #Inicio del ciclo
    while finish == False:
        if len(unvisited_nodes) == 0: #No hay más nodos a visitar
            finish = True
            
        else:
            #Obtenemos el nodo con el menor f-score de los NO VISITADOS
            current_node, minm = min_fscore(unvisited_nodes, current_node, parents)

            #print("El mínimo fscore es:",minm)
            #print("Siguiente nodo es:",current_node)
            #Revisamos si llegamos a la meta
            if current_node == target_node:
                finish = True
                print("Agregando nodo",current_node,"a visitados")
                print("SUCCESS")
                #Copiamos los datos a la lista de visitados
                visited_nodes[current_node] = unvisited_nodes[current_node]
            else:
                #Examinamos los vecinos
                #print()
                #print("*************************************************************")
                #print("Estoy en nodo:", current_node)
                #print("Nodo pasado es:", past_node)
                #print("Examinando vecinos")
                for nbr in grafo[current_node]:
                    if nbr not in visited_nodes:
                        #print("Revisando vecnio:", nbr)
                        #print("Calculando ruta óptima")
                        #Calculamos la nueva g-score
                        new_gscore = unvisited_nodes[current_node][g_score] + grafo[current_node][nbr]

                        #Revisamos si el nuevo gscore es menor
                        if new_gscore < unvisited_nodes[int(nbr)][g_score]:
                            #print(new_gscore,"Es menor que",unvisited_nodes[int(nbr)][g_score])
                            unvisited_nodes[int(nbr)][g_score] = new_gscore
                            unvisited_nodes[int(nbr)][f_score] = new_gscore + heuristic[int(nbr)]
                            #Agregamos el nodo actual al previo del vecino
                            unvisited_nodes[int(nbr)][previous] = current_node
                            parents.append(current_node)
                            #print("fscore de nodo",nbr, "=",new_gscore + heuristic[int(nbr)])
                        #else:
                            #print("No es menor")
                            
                #Agregamos el nodo actual a la lista de VISITADOS
                visited_nodes[current_node] = unvisited_nodes[current_node]
                #print("Agregando nodo",current_node,"a visitados")
                #Lo eliminamos de la lista de NO VISITADOS
                del(unvisited_nodes[current_node])

    path = []
    for key in visited_nodes:
        path.append(key)

    return visited_nodes, path
    
        

    
dic, path = A_star(grafo)
print("El path es:", path)
print(dic)
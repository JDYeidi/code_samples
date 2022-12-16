#Importamos librerías pandas para leer los archivos CSV
import pandas as pd
import numpy as np

#Leemos el dataframe
df_edges = pd.read_csv("edges.csv")
df_nodes = pd.read_csv("nodes.csv")

#Nodos
#nodos = df_nodes.iloc[:,0:1]
#nodos = nodos.to_numpy()
nodos = [1,2,3,4,5,6,7,8,9,10,11,12]
Heuristic = df_nodes.iloc[:,3]
Heuristic = Heuristic.to_numpy()
#Heuristic = [1.4142, 1.0762, 1.1244, 0.8494, 0.7604, 0.8927, 0.5719, 0.5014, 0.6134, 0.3135, 0.214, 0]
vecinos = df_edges.iloc[:,0:2]
vecinos = vecinos.to_numpy()
costo = df_edges.iloc[:,2]
costo = costo.to_numpy()



#Inicializamos lista de nodos abierta y cerrada 
open_list = []
close_list = []
#Inicializamos variables que vamos a necesitar
inicial_node = 1
goal_node = 12
past_cost = [0,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000]
parent = [0,0,0,0,0,0,0,0,0,0,0,0]
path = [1]



#Agregamos el nodo inicial a la lista de nodos abiertos
open_list.append(inicial_node)

while len(open_list) > 0:
    #Nodo actual es igual al primer nodo en la lista OPEN
    current = open_list[0]
    #Eliminamos el primero nodo de OPEN
    open_list.pop(0)
    #Agregamos el nodo CURRENT a la lista CLOSE
    close_list.append(current)
    print(close_list)
    #Revisamos si llegamos a la meta
    if current == goal_node:
        print("SUCCESS")
        #Calculo del path
        break
    
    #Creamos lista para guardar los vecinos del nodo actual
    current_neighbours = []
    current_cost = []
    est_total_cost = [1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000]
    contador = 0 

    #Recorremos las columnas de nodos y sus vecinos
    for i in vecinos:
        #Condición para elegir el vecino del nodo
        if current in i:
            #Si la posición es igual al nodo actual entonces el vecino es la posición 1
            if i[0] == current:
                current_neighbours.append(i[1])
                current_cost.append(costo[contador])
            else:
                current_neighbours.append(i[0])
                current_cost.append(costo[contador])

        contador += 1

    #Para cada vecino del nodo actual que no está en la lista CLOSE
    for i in current_neighbours:
        if i not in close_list:
            print("Current:", current)
            print("Calculando para", i)
            print("tentative_past_cost =", past_cost[nodos.index(current)], "+",current_cost[current_neighbours.index(i)])
            tentative_past_cost = past_cost[nodos.index(current)] + current_cost[current_neighbours.index(i)]

            if tentative_past_cost < past_cost[nodos.index(i)]:
                past_cost[nodos.index(i)] = tentative_past_cost 
                print("El past_cost de: ", i, tentative_past_cost)
                parent[nodos.index(i)] = current
                print("Indice",nodos.index(i))
                est_total_cost[nodos.index(i)] = past_cost[nodos.index(i)] + Heuristic[nodos.index(i)-1]
                print("El costo total de: ", i, est_total_cost[nodos.index(i)])
                
    cost_min = min(est_total_cost)
    path.append(nodos[est_total_cost.index(cost_min)])
    open_list.append(nodos[est_total_cost.index(cost_min)])
    
    
                
                
                
            





import pandas as pd

class create_graph():
    def __init__(self, edges, nodes):
        self.edges = edges
        self.nodes = nodes

    def main(self):
        #Leemos el dataframe
        df_edges = pd.read_csv(self.edges, header=None)
        df_nodes = pd.read_csv(self.nodes, header=None)
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

        return grafo, heuristic



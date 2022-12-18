from create_graph import create_graph


class A_star():
    def __init__(self, start_node, target_node, edges = None, nodes = None, graph = None, heuristic_dic = None):
        self.start_node = start_node
        self.target_node = target_node
        self.edges = edges
        self.nodes = nodes
        self.graph = graph
        self.heuristic_dic = heuristic_dic
        self.G_SCORE = 0
        self.F_SCORE = 1
        self.PREVIOUS = 2

    def get_heuristic(self,node, heuristic_dic):
        return heuristic_dic[node]

    def get_minimum(self, unvisited):
        fscore_minimum = 1000000
        unv_key = None

        for node in unvisited.items():
            fscore = node[1][self.F_SCORE]
            if fscore < fscore_minimum:
                fscore_minimum = fscore
                unv_key = node[0]

        return unv_key
        

    def main(self):
        if self.edges != None and self.nodes != None:
            graph, heuristic_dic = create_graph(self.edges, self.nodes).main()
        elif self.graph != None:
            graph = self.graph
            heuristic_dic = self.heuristic_dic

        #Diccionarios de nodos visitados y no visitados
        visited = {}
        unvisited = {}

        #Agregar e incializar cada nodo de los no visitados
        for node in graph:
            #Inicializa g-score and f-score al infinito
            #Nodo previo a NULL
            unvisited[node] = [1000000, 1000000, None]

        #Actualizamos los valores del nodo inicial en la lista de no visitados
        f_score_value = self.get_heuristic(self.start_node, heuristic_dic)
        #print(f"f_score del nodo inicial: {f_score_value}")
        unvisited[self.start_node] = [0, f_score_value, None]

        #Repetimos hasta que no queden nodos en no visitados
        finished = False
        while finished == False:
            #Vueltas
            iteracion = 0
            #print(f"Iteración número: {iteracion}")
            #print(f"Lista de nodos visitados: {visited}")
            #print(f"Lista de nodos NO visitados: {unvisited}")
            #Revisamos si no quedan nodos por visitar
            if len(unvisited) == 0:
                finished == True

            else:
                #Regresamos el nodo no visitado con el f-score menor
                current_node = self.get_minimum(unvisited)
                #print(f"Nodo actual con minimo fscore: {current_node}")
                #Revisamos si el nodo actual es el nodo objetivo
                if current_node == self.target_node:
                    #Agregamos el nodo a los visitados
                    finished = True
                    visited[current_node] = unvisited[current_node]
                else:
                    #Obtenemos la lista de vecinos del nodo actual
                    neighbours = graph[current_node]
                    #print(f"Vecinos del nodo actual: {neighbours}")
                    #Repetimos para cada vecino en la lista de vecinos
                    for node in neighbours:
                        #Revisamos si el nodo vecino ya se ha visitado
                        if node not in visited:
                            #Calculamos la nueva g-score
                            new_g_score = unvisited[current_node][self.G_SCORE] + neighbours[node]
                            #print(f"new_g_score: {new_g_score}")
                            #print(f"gscore del nodo vecino {node}: {unvisited[node][self.G_SCORE]}")
                            #Revisamos si la nueva g-score es menor
                            if new_g_score < unvisited[node][self.G_SCORE]:
                                #Actualizamos g-score, f-score y el nodo previo 
                                unvisited[node][self.G_SCORE] = new_g_score
                                unvisited[node][self.F_SCORE] = new_g_score + self.get_heuristic(node, heuristic_dic)
                                #print(f"Nueva fscore del nodo {node}: {unvisited[node][self.F_SCORE]} ")
                                unvisited[node][self.PREVIOUS] = current_node
                    #Agregamos el nodo actual a los visitados
                    visited[current_node] = unvisited[current_node]
                    #Eliminamos el nodo actual de los no visitados
                    del unvisited[current_node]
                    iteracion += 1

        return visited 
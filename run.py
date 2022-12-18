from A_star import A_star
graph = {
           "A": {"B":10, "C":12, "D":5},
           "B": {"A":10, "E":11},
           "C": {"A":12, "D":6, "E":11},
           "D": {"A":5, "C":6, "F":14},
           "E": {"B":11, "C":11},
           "F": {"C":8, "D":14}
         }
heuristic_dic = {"A":10, "B":15, "C":5, "D":5, "E":10, "F":0}
if __name__ == '__main__':
    #A_star(edges, nodes, graph)
    #path = A_star("A","F", graph = graph, heuristic_dic=heuristic_dic)
    path = A_star(1,12, edges='edges.csv', nodes='nodes.csv')
    path = path.main()
    print(f"El camino más óptimo es el siguiente: {path}")
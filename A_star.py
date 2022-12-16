from create_graph import create_graph




class A_star():
    def __init__(self, start_node, target_node, edges = None, nodes = None, graph = None):
        self.start_node = start_node
        self.target_node = target_node
        self.edges = edges
        self.nodes = nodes
        self.graph = graph

    def main(self):
        if self.edges != None and self.nodes != None:
            graph, heuristic_dic = create_graph(self.edges, self.nodes).main()
        elif self.graph != None:
            graph = self.graph
        print(graph)
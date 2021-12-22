from GraphAlgo import GraphAlgo
from DiGraph import DiGraph

if __name__ == '__main__':
    graph = GraphAlgo()
    graph.load_from_json("A1.json")
    graph.plot_graph()
    graph.get_graph().remove_edge(16, 15)
    graph.get_graph().remove_edge(15, 16)
    graph.plot_graph()

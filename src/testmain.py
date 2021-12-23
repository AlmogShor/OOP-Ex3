from GraphAlgo import GraphAlgo
from DiGraph import DiGraph

if __name__ == '__main__':
    graph = GraphAlgo()
    graph.load_from_json("A1.json")
    graph.plot_graph()

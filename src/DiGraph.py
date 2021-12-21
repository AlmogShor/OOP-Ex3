from src.GraphInterface import GraphInterface
from src.node_data import node_data as node
from src.edge_data import edge_data as edge


class DiGraph(GraphInterface):

    def __init__(self):
        self.__nodes = {}
        self.__in_edges = {}
        self.__out_edges = {}
        self.__MC = 0

    def v_size(self) -> int:
        return self.__nodes.__sizeof__()

    def e_size(self) -> int:
        count = 0
        for i in self.__out_edges:
            count += i.__sizeof__()
        return count

    def get_all_v(self) -> dict:
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.__in_edges.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__out_edges.get(id1)

    def get_mc(self) -> int:
        return self.__MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.__nodes.get(id1) is None or self.__nodes.get(id2) is None:
            return False
        if self.__out_edges.get(id1) is None:
            self.__out_edges[id1] = {}
        if self.__in_edges.get(id2) is None:
            self.__in_edges[id2] = {}
        if self.__out_edges[id1].get(id2) is None:
            self.__out_edges[id1][id2] = weight
            self.__in_edges[id2][id1] = weight
            self.__MC += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.__nodes.get(node_id) is not None:
            return False
        self.__nodes[node_id] = node(node_id, pos)
        self.__MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.__nodes.get(node_id) is None:
            return False
        self.__nodes.pop(node_id)
        self.__MC += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.__nodes.get(node_id1) is None or self.__nodes.get(node_id2) is None:
            return False
        if self.__out_edges.get(node_id1) is None:
            return False
        if self.__out_edges[node_id1].get(node_id2) is None:
            return False
        self.__out_edges[node_id1].pop(node_id2)
        self.__in_edges[node_id2].pop(node_id1)
        self.__MC += 1
        return True

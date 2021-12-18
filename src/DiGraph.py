from src.GraphInterface import GraphInterface
from src.node_data import node_data as node
from src.edge_data import edge_data as edge


class DiGraph(GraphInterface):

    def __init__(self):
        self.__nodes = dict.fromkeys([node])
        self.__edges = dict.fromkeys([edge])
        self.__toMe = dict.fromkeys(dict.fromkeys([edge]))
        self.__MC = 0

    def v_size(self) -> int:
        return self.__nodes.__sizeof__()

    def e_size(self) -> int:
        return self.__edges.__sizeof__()

    def get_all_v(self) -> dict:
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return super().all_in_edges_of_node(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return super().all_out_edges_of_node(id1)

    def get_mc(self) -> int:
        return self.__MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        self.__edges[id1] = edge(id1, id2, weight)
        if self.__edges[id1] is None:
            return False
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        self.__nodes[node_id] = node(node_id, pos)
        if self.__nodes[node_id] is None:
            return False
        return True

    def remove_node(self, node_id: int) -> bool:
        self.__nodes[node_id] = None
        if self.__nodes[node_id] is not None:
            return False
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        self.__edges[node_id1] = None
        if self.__edges[node_id1] is not None:
            return False
        return True

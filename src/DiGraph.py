from GraphInterface import GraphInterface
from node_data import node_data as node


class DiGraph(GraphInterface):

    def __init__(self):
        self.__nodes = {}
        self.__in_edges = {}
        self.__out_edges = {}
        self.__MC = 0

    def v_size(self) -> int:
        return len(self.__nodes)

    def e_size(self) -> int:
        count = 0
        for i in self.__out_edges.values():
            count += len(i)
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

    def add_node(self, node_id: int, pos: tuple = (0.0, 0.0, 0.0)) -> bool:
        if self.__nodes.get(node_id) is not None:
            return False
        self.__nodes[node_id] = node(node_id, pos)
        self.__MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.__nodes.get(node_id) is None:
            return False
        if self.all_out_edges_of_node(node_id) is not None:
            for out in self.all_out_edges_of_node(node_id).keys():
                self.__in_edges.get(out).pop(node_id)
                if len(self.__in_edges.get(out)) == 0:
                    self.__in_edges.pop(out)
            self.__out_edges.pop(node_id)
        if self.all_in_edges_of_node(node_id) is not None:
            for toMe in self.all_in_edges_of_node(node_id).keys():
                self.__out_edges.get(toMe).pop(node_id)
                if len(self.__out_edges.get(toMe)) == 0:
                    self.__out_edges.pop(toMe)
            self.__in_edges.pop(node_id)
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
        if len(self.__out_edges.get(node_id1)) == 0:
            self.__out_edges.pop(node_id1)
        self.__in_edges[node_id2].pop(node_id1)
        if len(self.__in_edges.get(node_id2)) == 0:
            self.__in_edges.pop(node_id2)
        self.__MC += 1
        return True

    def distance(self, current_min_node, neighbor):
        # tmp = self.__in_edges[current_min_node][neighbor]
        # #tmp.get_weight
        # #return tmp
        return None

    def __str__(self):
        return "Graph: |V|=" + str(self.v_size()) + ", |E|=" + str(self.e_size())

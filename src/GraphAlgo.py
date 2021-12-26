import json
import string
from queue import PriorityQueue
from random import random, seed

from typing import List, cast

from matplotlib import pyplot as plt

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from node_data import node_data
import sys
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        if g is None:
            self.__DiGraph = DiGraph()
        else:
            self.__DiGraph = g

    def get_graph(self) -> GraphInterface:
        return self.__DiGraph

    def load_from_json(self, file_name: str) -> bool:
        try:
            f = open(file_name)
            self.get_graph().__init__()
            data = json.load(f)
            for i in data["Nodes"]:
                if "pos" in data["Nodes"]:
                    s = (i["pos"])
                    s: cast(string, s)  # casing to string
                    t = s.split(',')  # spliting to nodes
                    tuplePos = (float(t[0]), float(t[1]), float(t[2]))
                    self.__DiGraph.add_node(i["id"], tuplePos)
                else:
                    tuplePos = (0.0, 0.0, 0.0)
                    self.__DiGraph.add_node(i["id"], tuplePos)
            for i in data["Edges"]:
                self.__DiGraph.add_edge(i["src"], i["dest"], i["w"])
            f.close()
            return True
        except Exception:
            return False

    def save_to_json(self, file_name: str) -> bool:
        data = {'Edges': [], 'Nodes': []}
        for node in self.get_graph().get_all_v().values():
            loc = node.get_location()
            data['Nodes'].append({
                'pos': ','.join(map(str, loc)),
                'id': node.get_key()
            })
            edgeDict = self.get_graph().all_out_edges_of_node(node.get_key())
            if edgeDict is not None:
                for dest in edgeDict.keys():
                    data['Edges'].append({
                        'src': node.get_key(),
                        'w': edgeDict[dest],
                        'dest': dest
                    })
        try:
            with open(file_name, 'w') as outfile:
                json.dump(data, outfile, indent=2)
        except Exception:
            print("error with open file")

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        weight, prev_node = self.dijkstra_algorithm(id1)
        path = []
        start = id2
        path.append(start)
        if weight[id2] != float('inf'):
            while start != id1:
                start = prev_node[start]
                path.append(start)
        else:
            path = []
        path.reverse()
        return weight[id2], path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if len(node_lst) == 0:
            return None
        ans: List[int] = []
        weight = 0
        idx_to_delete = 0
        here = node_lst[idx_to_delete]
        node_lst.remove(node_lst[0])
        while len(node_lst) > 0:
            curr_min = sys.float_info.max
            routes, curr_shortest_path = self.dijkstra_algorithm(here)
            for i in range(len(node_lst)):
                if (routes[node_lst[i]] < curr_min):
                    curr_min = routes[node_lst[i]]
                    idx_to_delete = i
            path = self.shortest_path(here, node_lst[idx_to_delete])
            ans.extend(path[1])
            ans.pop(len(ans) - 1)
            here = node_lst[idx_to_delete]
            node_lst.remove(node_lst[idx_to_delete])
            weight = weight + curr_min

        ans.append(here)
        return ans, weight

    def centerPoint(self) -> (int, float):
        ans = node_data(-2, (1, 2, 3))
        curr_min = sys.float_info.max
        nodes = self.__DiGraph.get_all_v()
        for value in nodes.values():
            curr_max = 0
            srcNode = value
            routes = self.dijkstra_algorithm(value.get_key())[0]  # need to wait for almog
            for key in routes:
                routes
                if key == sys.float_info.max:
                    return None
                if key > curr_max:
                    curr_max = key
            if curr_max < curr_min:
                curr_min = curr_max
                ans = srcNode
        return ans.get_key(), curr_min

    def plot_graph(self) -> None:
        x = []
        y = []
        for node in self.get_graph().get_all_v().values():
            x.append(node.get_location()[0])
            y.append(node.get_location()[1])
        plt.plot(x, y, 'ro')
        for i in range(len(x)):
            plt.annotate(i, xy=(x[i] * 0.999991, y[i] * 1.000005))
        for node_id in self.get_graph().get_all_v().keys():
            if (self.get_graph().all_out_edges_of_node(node_id) is not None):
                for edge in self.get_graph().all_out_edges_of_node(node_id).keys():
                    dest_x = self.get_graph().get_all_v().get(edge).get_location()[0]
                    dest_y = self.get_graph().get_all_v().get(edge).get_location()[1]
                    src_x = self.get_graph().get_all_v().get(node_id).get_location()[0]
                    src_y = self.get_graph().get_all_v().get(node_id).get_location()[1]
                    plt.annotate("", xy=(src_x, src_y), xytext=(dest_x, dest_y),
                                 arrowprops={'arrowstyle': "<-", 'lw': 2})
        plt.show()

    def dijkstra_algorithm(self, start_node):
        weight = list(self.__DiGraph.get_all_v())
        prev_nodes = list(self.__DiGraph.get_all_v())
        queue = PriorityQueue()
        for node in weight:
            weight[node] = float('inf')
        weight[start_node] = 0
        for p in prev_nodes:
            prev_nodes[p] = -1
        queue.put(start_node, 0)
        while not queue.empty():
            node = queue.get()
            edges = self.__DiGraph.all_out_edges_of_node(node)
            if edges != None:
                for edge in edges.keys():
                    if weight[node] + edges.get(edge) < weight[edge]:
                        weight[edge] = weight[node] + edges.get(edge)
                        queue.put(edge, weight[edge])
                        prev_nodes[edge] = node
        return weight, prev_nodes

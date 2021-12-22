import json
import string
from typing import List, cast

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
                s = (i["pos"])
                s: cast(string, s)  # casing to string
                t = s.split(',')  # splitting to nodes
                tuple_pos = (float(t[0]), float(t[1]), float(t[2]))
                self.__DiGraph.add_node(i["id"], tuple_pos)
            for i in data["Edges"]:
                self.__DiGraph.add_edge(i["src"], i["dest"], i["w"])
            f.close()
            return True
        except Exception:
            return False

    def save_to_json(self, file_name: str) -> bool:
        data = {'Edges': [], 'Nodes': []}
        # data['Edges'] = []
        # data['Nodes'] = []
        for node in self.get_graph().get_all_v().values():
            loc = node.get_location()
            data['Nodes'].append({
                'pos': ','.join(map(str, loc)),
                'id': node.get_key()
            })
            edge_dict = self.get_graph().all_out_edges_of_node(node.get_key())
            for dest in edge_dict.keys():
                data['Edges'].append({
                    'src': node.get_key(),
                    'w': edge_dict[dest],
                    'dest': dest
                })
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile, indent=2)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        prev_nodes, curr_shortest_path = self.dijkstra_algorithm(id1)
        return (curr_shortest_path, prev_nodes)


    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if node_lst.__sizeof__() == 0:
            return None
        ans: List[int] = []
        idx_to_delete = 0
        here = node_lst[0]
        node_lst.remove(node_lst[0])
        while node_lst.__sizeof__() > 0:
            min = sys.float_info.max
            routes, curr_shortest_path = self.dijkstra_algorithm(here)
            for i in node_lst:
                if routes[node_lst[i]] < min:
                    min = routes[node_lst[i]]
                    idx_to_delete = i
            path = self.shortest_path(here, node_lst[idx_to_delete])
            ans.__add__(path)
            del ans[-1]
            here = node_lst[idx_to_delete]
            node_lst.remove(node_lst[idx_to_delete])

        ans.__add__(here)
        return ans

    def centerPoint(self) -> (int, float):
        ans = node_data(None)
        min = sys.float_info.max
        nodes = self.__DiGraph.get_all_v()
        for key in nodes:
            max = 0
            srcNode = nodes[key]
            routes = self.dijkstra_algorithm([key])  # need to wait for almog
            for key1 in routes:
                if routes[key1] == -1:
                    return None
                if routes[key1] > max:
                    max = routes[key1]
            if max < min:
                min = max
                ans = srcNode
        return ans.get_key(), min

    def plot_graph(self) -> None:
        pass

    # Almog place

    def dijkstra_algorithm(self, start_node):

        unvisited_nodes = list(self.__DiGraph.get_all_v())

        # Using dict to save the weight of visiting each node and update it as we move along the graph
        shortest_path = {}

        # Using dict to save the shortest known path to a node found so far
        previous_nodes = {}

        # We'll use max_value to initialize the "infinity" value of the unvisited nodes
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0
        shortest_path[start_node] = 0.0

        # The algorithm executes until we visit all nodes
        while unvisited_nodes:
            # The code block below finds the node with the lowest score
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = self.__DiGraph.all_out_edges_of_node(current_min_node)
            for neighbor in neighbors.keys():
                tentative_value = shortest_path[current_min_node] + neighbors[neighbor]  # distance(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node

                    # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path

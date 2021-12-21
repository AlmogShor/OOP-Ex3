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
            f = open("C:\\Users\\Sabrina\\PycharmProjects\\OOP-Ex3\\src\\A1.json")
            data = json.load(f)
            for i in data["Nodes"]:
                s = (i["pos"])
                s: cast(string, s)  # casing to string
                t = s.split(',')  # spliting to nodes
                tuplePos = (float(t[0]), float(t[1]), float(t[2]))
                self.__DiGraph.add_node(i["id"], tuplePos)
            for i in data["Edges"]:
                self.__DiGraph.add_edge(i["src"], i["dest"], i["w"])
            f.close()
            return True
        except Exception:
            return False

    def save_to_json(self, file_name: str) -> bool:
        dictEdge = {'Edges'}
        dictEdge['Edges'] = {}
        dict= dictEdge['Edges']
        for i in self.__DiGraph.get_all_v().keys():
            x= self.__DiGraph.get_all_v(i)
            dict.update(x)



        b = self.__DiGraph.get_all_v()
        b = self.__DiGraph.all_in_edges_of_node(1)
        c = json.dumps(dict, indent=2)
        with open('data.json', 'w') as fp:
            fp.write(c)
        # a_file = json.dump(self.__DiGraph., a_file)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if (node_lst.__sizeof__() == 0):
            return None
        ans: List[int] = []
        idxToDelete = 0
        here = node_lst[0]
        node_lst.remove(node_lst[0])
        while node_lst.__sizeof__() > 0:
            min = sys.float_info.max
            routes = self.johnson()[here]  # need to ask almog
            for i in node_lst:
                if (routes[node_lst[i]] < min):
                    min = routes[node_lst[i]]
                    idxToDelete = i
            path = self.shortest_path(here, node_lst[idxToDelete])
            ans.__add__(path)
            del ans[-1]
            here = node_lst[idxToDelete]
            node_lst.remove(node_lst[idxToDelete])

        ans.__add__(here)
        return ans

    def centerPoint(self) -> (int, float):
        ans = node_data(None)
        min = sys.float_info.max
        nodes = self.__DiGraph.get_all_v()
        for key in nodes:
            max = 0
            srcNode = nodes[key]
            routes = self.johnson()[key]  # need to wait for almog
            for key1 in routes:
                if (routes[key1] == -1):
                    return None;
                if (routes[key1] > max):
                    max = routes[key1]
            if (max < min):
                min = max
                ans = srcNode
        return ans.get_key(), min;

    def plot_graph(self) -> None:
        pass

    # almog place
    def johnson(self) -> (dict):
        """Return distance where distance[u][v] is the min distance from u to v.

        distance[u][v] is the shortest distance from vertex u to v.

        self is a Graph object which can have negative edge weights.
        """
        # add new vertex q
        self.__DiGraph.add_node()
        # let q point to all other vertices in self with zero-weight edges
        for v in self.__DiGraph.get_all_v:
            self.add_edge('q', v.get_key(), 0)

        # compute shortest distance from vertex q to all other vertices
        bell_dist = self.bellman_ford(self, self.get_vertex('q'))

        # set weight(u, v) = weight(u, v) + bell_dist(u) - bell_dist(v) for each
        # edge (u, v)
        for v in self:
            for n in v.get_neighbours():
                w = v.get_weight(n)
                v.set_weight(n, w + bell_dist[v] - bell_dist[n])

        # remove vertex q
        # This implementation of the graph stores edge (u, v) in Vertex object u
        # Since no other vertex points back to q, we do not need to worry about
        # removing edges pointing to q from other vertices.

        # distance[u][v] will hold smallest distance from vertex u to v
        distance = {}
        # run dijkstra's algorithm on each source vertex
        for v in self.__DiGraph.get_all_v():
            distance[v] = self.dijkstra(self, v)

        # correct distances
        for v in self.__DiGraph.get_all_v():
            for w in self.__DiGraph.get:
                distance[v][w] += bell_dist[w] - bell_dist[v]

        # correct weights in original graph
        for v in self.__DiGraph.get_all_v():
            for n in v.get_neighbours():
                w = v.get_weight(n)
                v.set_weight(n, w + bell_dist[n] - bell_dist[v])

        return distance

    def bellman_ford(self, source):
        """Return distance where distance[v] is min distance from source to v.

        This will return a dictionary distance.

        self is a Graph object which can have negative edge weights.
        source is a Vertex object in self.
        """
        distance = dict.fromkeys(self, float('inf'))
        distance[source] = 0

        for _ in range(len(self) - 1):
            for v in self.__DiGraph.get_all_v():
                for n in v.get_neighbours():
                    distance[n] = min(distance[n], distance[v] + v.get_weight(n))

        return distance

    def dijkstra(self, source):
        """Return distance where distance[v] is min distance from source to v.

        This will return a dictionary distance.

        self is a Graph object.
        source is a Vertex object in self.
        """
        unvisited = set(self)
        distance = dict.fromkeys(self, float('inf'))
        distance[source] = 0

        while unvisited != set():
            # find vertex with minimum distance
            closest = min(unvisited, key=lambda v: distance[v])

            # mark as visited
            unvisited.remove(closest)

            # update distances
            for neighbour in closest.get_neighbours():
                if neighbour in unvisited:
                    new_distance = distance[closest] + closest.get_weight(neighbour)
                    if distance[neighbour] > new_distance:
                        distance[neighbour] = new_distance

        return distance
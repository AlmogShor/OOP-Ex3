import unittest
import sys

from src.node_data import node_data
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GraphAlgo import GraphAlgo
from src.GraphAlgoInterface import GraphAlgoInterface
sys.path.append('C:\\Users\\shora\\PycharmProjects\\OOP-Ex3\\src')


class MyTestCase(unittest.TestCase):
    def test_get_graph(self):
        Graph = GraphAlgo()
        Graph.load_from_json('A1.json')
        g = Graph.get_graph().v_size()
        self.assertEqual(11, g)  # add assertion here
        g = Graph.get_graph().e_size()
        self.assertEqual(22, g)
        Graph.save_to_json("a")


if __name__ == '__main__':
    unittest.main()

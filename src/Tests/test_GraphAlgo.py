import unittest
import sys
sys.path.append('C:\\Users\\barak\\PycharmProjects\\OOP-Ex3\\src')

from src.node_data import node_data
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GraphAlgo import GraphAlgo
from src.GraphAlgoInterface import GraphAlgoInterface



class MyTestCase(unittest.TestCase):
    def test_get_graph(self):
        Graph = GraphAlgo()
        Graph.load_from_json("C:\\Users\\barak\\PycharmProjects\\OOP-Ex3\\src\\A1.json")
        g = Graph.get_graph().v_size()
        self.assertEqual(17, g)  # add assertion here
        g = Graph.get_graph().e_size()
        self.assertEqual(36, g)
        Graph.save_to_json("a")


if __name__ == '__main__':
    unittest.main()

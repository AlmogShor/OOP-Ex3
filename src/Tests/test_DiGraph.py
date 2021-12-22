import unittest
import sys
sys.path.append('C:\\Users\\barak\\PycharmProjects\\OOP-Ex3\\src')

from src.node_data import node_data
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface

sys.path.append('OOP-Ex3\\src')


class MyTestCase(unittest.TestCase):
    def test_v_size(self):
        graph1 = DiGraph()
        self.assertEqual(0, graph1.v_size())  # add assertion here
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        graph1.add_node(0, point1)
        self.assertEqual(1, graph1.v_size())
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph1.add_node(1, point2)
        self.assertEqual(2, graph1.v_size())

    def test_e_size(self):
        graph1 = DiGraph()
        self.assertEqual(0, graph1.e_size())
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph1.add_node(1, point2)
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        graph1.add_node(0, point1)
        graph1.add_edge(0, 1, 3)
        self.assertEqual(1, graph1.e_size())
        graph1.add_edge(1, 0, 5)
        self.assertEqual(2, graph1.v_size())

    def test_get_all_v(self):
        graph1 = DiGraph()
        n = graph1.get_all_v()
        self.assertEqual(None, n.get(0))
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        graph1.add_node(0, point1)
        self.assertEqual(0, n.get(0).get_key())
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph1.add_node(1, point2)
        self.assertEqual(1, n.get(1).get_key())
        self.assertEqual(35.18958953510896, n.get(1).get_location()[0])
        self.assertEqual(None, n.get(4))
        # n = all_in_edges_of_node()

    def test_all_in_edges_of_node(self):
        graph1 = DiGraph()
        self.assertEqual(0, graph1.e_size())
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph1.add_node(1, point2)
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        graph1.add_node(0, point1)
        graph1.add_edge(0, 1, 3)
        n = graph1.all_in_edges_of_node(1)
        self.assertEqual(3, n.get(0))
        graph1.add_edge(1, 0, 5)
        n = graph1.all_in_edges_of_node(0)
        self.assertEqual(5, n.get(1))

    def test_all_out_edges_of_node(self):
        graph1 = DiGraph()
        n = graph1.all_out_edges_of_node(0)
        self.assertEqual(None, n)
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph1.add_node(1, point2)
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        graph1.add_node(0, point1)
        graph1.add_edge(0, 1, 3)
        n = graph1.all_out_edges_of_node(0)
        self.assertEqual(3, n.get(1))
        graph1.add_edge(1, 0, 5)
        n = graph1.all_out_edges_of_node(0)
        self.assertEqual(3, n.get(1))

    def test_get_mc(self):
        graph1 = DiGraph()
        self.assertEqual(0, graph1.get_mc())
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph1.add_node(1, point2)
        self.assertEqual(1, graph1.get_mc())
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        graph1.add_node(0, point1)
        self.assertEqual(2, graph1.get_mc())
        graph1.add_edge(0, 1, 3)
        self.assertEqual(3, graph1.get_mc())

    def test_add_edge(self):
        graph1 = DiGraph()
        self.assertEqual(0, graph1.e_size())
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph1.add_node(1, point2)
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        graph1.add_node(0, point1)
        graph1.add_edge(0, 1, 3)
        n = graph1.all_in_edges_of_node(1)
        self.assertEqual(3, n.get(0))
        n = graph1.all_in_edges_of_node(0)
        self.assertEqual(None, n)
        n = graph1.all_out_edges_of_node(0)
        self.assertEqual(3, n.get(1))
        n = graph1.all_out_edges_of_node(1)
        self.assertEqual(None, n)

    def test_add_node(self):
        graph1 = DiGraph()
        n = graph1.get_all_v()
        self.assertEqual(None, n.get(0))
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        graph1.add_node(0, point1)
        self.assertEqual(0, n.get(0).get_key())
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph1.add_node(1, point2)
        self.assertEqual(1, n.get(1).get_key())
        self.assertEqual(35.18958953510896, n.get(1).get_location()[0])
        self.assertEqual(None, n.get(4))

    def test_remove_node(self):
        graph1 = DiGraph()
        n = graph1.get_all_v()
        self.assertEqual(None, n.get(0))
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        graph1.add_node(0, point1)
        self.assertEqual(0, n.get(0).get_key())
        graph1.remove_node(0)
        n = graph1.get_all_v()
        self.assertEqual(None, n.get(0))
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        graph1.add_node(1, point2)
        self.assertEqual(1, n.get(1).get_key())
        self.assertEqual(35.18958953510896, n.get(1).get_location()[0])
        check = graph1.remove_node(1)
        self.assertEqual(True, check)
        n = graph1.get_all_v()
        self.assertEqual(None, n.get(1))
        check = graph1.remove_node(3)
        self.assertEqual(False, check)
        self.assertEqual(None, n.get(4))


if __name__ == '__main__':
    unittest.main()

import sys
import unittest

sys.path.append('C:\\Users\\barak\\PycharmProjects\\OOP-Ex3\\src')

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def generate(self) -> GraphAlgo:
        g = DiGraph()
        point1 = (0, 0, 0)
        point2 = (1, 6, 0)
        point3 = (4, 5, 0)
        point4 = (-1, 4, 0)
        point5 = (3, 0, 0)
        point6 = (2, -2, 0)
        point7 = (-1, -8, 0)
        point8 = (-6, -6, 0)
        point9 = (-7, -1, 0)
        point10 = (-4, -1, 0)
        g.add_node(0, point1)
        g.add_node(1, point2)
        g.add_node(2, point3)
        g.add_node(3, point4)
        g.add_node(4, point5)
        g.add_node(5, point6)
        g.add_node(6, point7)
        g.add_node(7, point8)
        g.add_node(8, point9)
        g.add_node(9, point10)
        g.add_edge(0, 1, 1.5)
        g.add_edge(0, 2, 20)
        g.add_edge(0, 3, 8.2)
        g.add_edge(0, 4, 5.2)
        g.add_edge(0,5,4.9)
        g.add_edge(0,6,2.3)
        g.add_edge(0,7,1.3)
        g.add_edge(0,8,0.4)
        g.add_edge(0,9,1.25)
        g.add_edge(9,1,4.2)
        g.add_edge(1,2,6.3)
        g.add_edge(2,3,1.2)
        g.add_edge(3,4,0.3)
        g.add_edge(4,5,5.3)
        g.add_edge(5,6,6.1)
        g.add_edge(6,7,4.3)
        g.add_edge(7,8,3.9)
        g.add_edge(8,9,9.2)
        g.add_edge(5, 0, 10)
        return g
    def test_get_graph(self):
        g = DiGraph()
        g = self.generate()
        gr = GraphAlgo(g)
        gl = GraphAlgo(g)
        grE= gr.get_graph().get_all_v()
        gE = gl.get_graph().get_all_v()
        for i in grE.keys():
            self.assertEqual(gE.get(i).get_key(), grE.get(i).get_key())
            self.assertEqual(gE.get(i).get_location(), grE.get(i).get_location())

        #Graph.save_to_json("a")

    def test_load_from_json(self):
        Graph = GraphAlgo()
        Graph.load_from_json("C:\\Users\\barak\\PycharmProjects\\OOP-Ex3\\src\\A1.json")
        g = Graph.get_graph().v_size()
        self.assertEqual(17, g)  # add assertion here
        g = Graph.get_graph().e_size()
        self.assertEqual(36, g)

    def test_save_to_json(self):
        Graph = GraphAlgo()
        Graph.load_from_json("C:\\Users\\barak\\PycharmProjects\\OOP-Ex3\\src\\A1.json")
        Graph.save_to_json('data.json')
        g= GraphAlgo()
        g.load_from_json('data.json')
        grE = g.get_graph().get_all_v()
        gE = Graph.get_graph().get_all_v()
        for i in grE.keys():
            self.assertEqual(gE.get(i).get_key(), grE.get(i).get_key())
            self.assertEqual(gE.get(i).get_location(), grE.get(i).get_location())

    def test_shortest_path(self):
        g = DiGraph()
        g = self.generate()
        gr = GraphAlgo(g)
        route = gr.shortest_path(2,4)
        self.assertEqual(route[0].get(4),1.5)
        route1 = gr.shortest_path(0, 2)
        self.assertEqual(route1[0].get(2), 7.8)
        route2 = gr.shortest_path(2, 6)
        self.assertAlmostEqual(route2[0].get(6),12.9)


    def test_centerPoint(self):
        g = DiGraph()
        g = self.generate()
        gr = GraphAlgo(g)
        self.assertEqual(gr.centerPoint()[0], 0)





if __name__ == '__main__':
    unittest.main()
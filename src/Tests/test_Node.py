import unittest
import sys
sys.path.append('..')
from src.node_data import node_data


class MyTestCase(unittest.TestCase):
    def test_Key(self):
        point1 = ("35.18753053591606", "32.10378225882353", "0.0")
        n = node_data(0, point1)
        point2 = ("35.18958953510896", "32.10785303529412", "0.0")
        n1 = node_data(1, point2)
        self.assertEqual(1, n1.get_key())
        # add assertion here

    def test_get_location(self):
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        n = node_data(0, point1)
        self.assertEqual(35.18753053591606, n.get_location()[0])
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        n1 = node_data(1, point2)
        self.assertEqual(35.18958953510896, n1.get_location()[0])

    def test_set_location(self):
        point1 = (35.18753053591606, 32.10378225882353, 0.0)
        n = node_data(0, point1)
        self.assertEqual(35.18753053591606, n.get_location()[0])
        point3 = (1, 2, 3)
        n.set_location(point3)
        self.assertEqual(2, n.get_location()[1])
        point2 = (35.18958953510896, 32.10785303529412, 0.0)
        n1 = node_data(1, point2)
        self.assertEqual(35.18958953510896, n1.get_location()[0])
        point4 = (2, 3, 4)
        n1.set_location(point4)
        self.assertEqual(4, n1.get_location()[2])


if __name__ == '__main__':
    unittest.main()

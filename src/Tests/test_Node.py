import unittest
import sys
sys.path.append('C:\\Users\\barak\\PycharmProjects\\OOP-Ex3\\src')
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

    def test_get_info(self):
        point1 = ("35.18753053591606", "32.10378225882353", "0.0")
        n = node_data(0, point1)
        self.assertEqual("", n.get_info())
        point2 = ("35.18958953510896", "32.10785303529412", "0.0")
        n1 = node_data(1, point2)
        self.assertEqual("", n1.get_info())

    def test_set_info(self):
        point1 = ("35.18753053591606", "32.10378225882353", "0.0")
        n = node_data(0, point1)
        self.assertEqual("", n.get_info())
        n.set_info("1")
        self.assertEqual("1", n.get_info())
        point2 = ("35.18958953510896", "32.10785303529412", "0.0")
        n1 = node_data(1, point2)
        self.assertEqual("", n1.get_info())
        n1.set_info("45")
        self.assertEqual("45", n1.get_info())

    def test_get_tag(self):
        point1 = ("35.18753053591606", "32.10378225882353", "0.0")
        n = node_data(0, point1)
        self.assertEqual(-1, n.get_tag())
        point2 = ("35.18958953510896", "32.10785303529412", "0.0")
        n1 = node_data(1, point2)
        self.assertEqual(-1, n1.get_tag())

    def test_set_tag(self):
        point1 = ("35.18753053591606", "32.10378225882353", "0.0")
        n = node_data(0, point1)
        self.assertEqual(-1, n.get_tag())
        n.set_tag(2)
        self.assertEqual(2, n.get_tag())
        point2 = ("35.18958953510896", "32.10785303529412", "0.0")
        n1 = node_data(1, point2)
        self.assertEqual(-1, n1.get_tag())
        n1.set_tag(2)
        self.assertEqual(2, n1.get_tag())

    def test_equals(self):
        point1 = ("35.18753053591606", "32.10378225882353", "0.0")
        n = node_data(0, point1)
        point3 = ("35.18753053591606", "32.10378225882353", "0.0")
        n2 = node_data(0, point3)
        self.assertEqual(True, n.equals(n2))
        point2 = ("35.18958953510896", "32.10785303529412", "0.0")
        n1 = node_data(1, point2)
        point4 = ("35.18958953510896", "32.10785303529412", "0.0")
        n3 = node_data(1, point4)
        self.assertEqual(True, n1.equals(n3))


if __name__ == '__main__':
    unittest.main()

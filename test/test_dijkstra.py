import unittest
import sys
import os

sys.path.append(os.path.abspath(sys.path[0]) + '/../')
import dijkstra

from test_fixtures import test_fixtures

class Djikstra_Tests(unittest.TestCase):

    longMessage = True

    def assert_path_equals(self, start, end, expected_path, expected_distance):
        path, distance = dijkstra.shortestPath(self.graph, start, end)
        self.assertEqual('-'.join(path), expected_path, 'path')
        self.assertEqual(distance, expected_distance, 'distance')

    def test_single_node(self):
        self.graph = test_fixtures['single_node']
        self.assert_path_equals('a', 'a', 'a', 0)

    def test_multinode(self):
        self.graph = test_fixtures['multinode']
        self.assert_path_equals('a', 'a', 'a', 0)
        self.assert_path_equals('a', 'd', 'a-d', 5)
        self.assert_path_equals('a', 'e', 'a-d-e', 7)
        self.assert_path_equals('e', 'a', 'e-a', 42)
        self.assert_path_equals('a', 'c', 'a-d-b-c', 9)

    def test_missing_node_throws(self):
        g = test_fixtures['multinode']
        self.assertRaises(ValueError, dijkstra.shortestPath, g, 'MISSING', 'a')
        self.assertRaises(ValueError, dijkstra.shortestPath, g, 'a', 'MISSING')
        self.assertRaises(ValueError, dijkstra.shortestPath, g, 'a', None)
        self.assertRaises(ValueError, dijkstra.shortestPath, g, None, 'a')

    def test_disjoint_graph_means_no_path_and_infinite_distance(self):
        self.graph = test_fixtures['disjoint']
        distances, predecessors = dijkstra.dijkstra(self.graph, '1_a', '2_c')
        self.assertIsNone(predecessors['2_c'])
        self.assertEqual(distances['2_c'], float('inf'))
        self.assert_path_equals('1_a', '2_c', '', float('inf'))

    def test_graph_with_node_referring_to_self_resolves_correctly(self):
        self.graph = test_fixtures['node_referring_to_self']
        self.assert_path_equals('b', 'b', 'b', 0)
        self.assert_path_equals('a', 'c', 'a-b-c', 2)

    def test_graph_with_internal_loop_resolves_correctly(self):
        self.graph = test_fixtures['internal_loop']
        self.assert_path_equals('a', 'c', 'a-b1-c', 2)

    def test_pathological_case(self):
        g = None
        self.assertRaises(TypeError, dijkstra.shortestPath, g, 'a', 'a')

    def test_bad_graph_missing_node_raises_error(self):
        g = test_fixtures['bad_graph_edge_to_missing_node']
        # backslashes required for parens, or regex tries to capture content.
        err_msg_regex = "missing node MISSING \(neighbor of a\)"
        self.assertRaisesRegexp(ValueError, err_msg_regex, dijkstra.shortestPath, g, 'a', 'b')

    def test_bad_graph_negative_edge_distance_raises_error(self):
        g = test_fixtures['bad_graph_negative_distance']
        err_msg_regex = "negative distance from b to c"
        self.assertRaisesRegexp(ValueError, err_msg_regex, dijkstra.shortestPath, g, 'a', 'c')

def main():
    unittest.main()

if __name__ == '__main__':
    main()

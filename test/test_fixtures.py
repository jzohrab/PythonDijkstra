# Data for tests and for graph generation.
test_fixtures = {
    'no_nodes': {},

    'single_node': {
        'a': {}
    },

    'multinode': {
        'a': {'b':10, 'd':5},
        'b': {'c':1, 'd':2},
        'c': {'e':4},
        'd': {'b':3, 'c':9, 'e':2},
        'e': {'a':42, 'c':6}
    },

    'disjoint': {
        '1_a': {'1_b':0},
        '1_b': {'1_a':0},
        '2_c': {'2_d':0},
        '2_d': {'2_c':0}
    },

    'node_referring_to_self': {
        'a': {'b':1},
        'b': {'b':1, 'c':1},
        'c': {}
    },

    'internal_loop': {
        'a': {'b1':1},
        'b1': {'b2':0, 'c':1},
        'b2': {'b1':0},
        'c': {}
    },

    'bad_graph_edge_to_missing_node': {
        'a': {'b':1, 'MISSING':10},
        'b': {}
    },

    'bad_graph_negative_distance': {
        'a': {'b':10},
        'b': {'c':-1},
        'c': {}
    }
}

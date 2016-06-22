def dijkstra(graph_dict, start, end):
    """Dijkstra's Shortest Path

    Args:
        graph_dict: a dictionary of dictionaries describing the
            graph. Top-level keys are node names, nested dicts are the
            connected neighbors and their distances. e.g.,
            "{'a':{'b':4},'b':{'a':2}}" describes a 2-node graph with each
            node connected to the other.
        start: the starting point for traversal
        end: the ending point

    Returns:
        (distances_from_start, predecessors)
        distances_from_start: dictionary of all nodes and their distances
            from the start
        predecessors: dictionary of nodes and their predecessors along
            the shortest path from start to end.  If there is no path from
            start to end, the predecessor of end is None.
    """

    if not start in graph_dict:
        raise ValueError('missing {0}'.format(start))
    if not end in graph_dict:
        raise ValueError('missing {0}'.format(end))

    nodes = graph_dict.keys()

    f = float('inf')
    dist_from_start = {n: f for n in nodes}  # dict comprehension, ref footnote 1
    dist_from_start[start] = 0
    predecessors = {n: None for n in nodes}

    while len(nodes) > 0:
        # Use the node closest to the start in this iteration.
        candidates = {n: dist_from_start[n] for n in nodes}
        closest = min(candidates, key = candidates.get)  # ref footnote 2

        for n in graph_dict[closest]:
            if not n in dist_from_start:
                msg = 'missing node {0} (neighbor of {1})'.format(n, closest)
                raise ValueError(msg)
            dist_to_n = graph_dict[closest][n]
            if dist_to_n < 0:
                msg = 'negative distance from {0} to {1}'.format(closest, n)
                raise ValueError(msg)
            d = dist_from_start[closest] + dist_to_n
            if dist_from_start[n] > d:
                dist_from_start[n] = d
                predecessors[n] = closest

        nodes.remove(closest)

    return (dist_from_start, predecessors)

    # Footnotes:
    #
    # 1. dict comprehension: ref https://www.python.org/dev/peps/pep-0274/
    #
    # 2. dict minimum: 'candidates' is an iterable, and 'key' is a
    # lambda function that takes the iteration value as an argument,
    # giving the sort order for the value.  'get' returns the value of
    # the dictionary.  So this one-liner sorts the 'candidates'
    # dictionary keys by their values, which are the dist_from_start
    # for that node.  ref
    # http://www.tutorialspoint.com/python/dictionary_get.htm


def shortestPath(graph_dict, start, end):
    """Output shortest path returned from dijkstra(graph_dict, start, end).

    Args:
        See dijkstra method for arg description.

    Returns:
        (path_array, total_distance)
    """
    distances, predecessors = dijkstra(graph_dict, start, end)

    # Handle no connected path from start to end.
    if predecessors[end] is None and start != end:
        return [], distances[end]

    path = [end]
    while path[-1] != start:
        path.append(predecessors[path[-1]])
    path.reverse()

    return path, distances[end]


# Sample
if __name__ == '__main__':
    from test import test_fixtures
    G = test_fixtures.test_fixtures['multinode']
    print 'The graph:'
    print(G)
    path, total_distance = shortestPath(G, 'a', 'e')
    msg = 'Shortest distance from a to e is {0}, total distance {1}.'
    print msg.format(' -> '.join(path), total_distance)

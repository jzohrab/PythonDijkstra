# Dijkstra's algorithm for shortest paths

Python implementation with tests.

There are a few Python implementations for this algorithm on the web,
(e.g.,
http://code.activestate.com/recipes/119466-dijkstras-algorithm-for-shortest-paths/).  This implementation:

* is extremely simple (is practically a direct mapping of how the
  algorithm would be done manually, ref
  https://www.youtube.com/watch?v=5GT5hYzjNoo), making it easier
  to adopt and modify for different domains
* handles some odd edge cases like disjoint graphs
* adds simple but descriptive error checks (e.g., for negative distances)
* has unit tests
* gives an example of GraphViz dotfiles from data

## Installation

This has been tested on Python 2.7.5.  There are no other dependencies.

## Usage

`dijkstra.py` is standalone and can be copied into any project and modified.

It provides an example:

```
$ python dijkstra.py 
The graph:
{'a': {'b': 10, 'd': 5}, 'c': {'e': 4}, 'b': {'c': 1, 'd': 2}, 'e': {'a': 42, 'c': 6}, 'd': {'c': 9, 'b': 3, 'e': 2}}
Shortest distance from a to e is a -> d -> e, total distance 7.
```

## Tests

Tests are in the `test` subfolder and can be run as follows:

```
$ python test/test_dijkstra.py 
```

## Dotfiles

The test fixtures in the tests directory can be converted to dotfiles:

```
test$ python generate_dotfiles.py
```

These can then be converted to png files using
[GraphViz](http://www.graphviz.org/Home.php):

```
$ dot -T png -O multinode.dot
```

Example:

![Sample](./sample_dotfile.png)

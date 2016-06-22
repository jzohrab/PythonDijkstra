import sys
import os

from test_fixtures import test_fixtures

def generate_dotfile_for_graph(filename, title, g):
    """Generates dotfile."""
    print "Generating " + filename
    header = "digraph " + title + """{
        rankdir = LR;
        size="8,5";
        node [shape = circle];
"""
    with open(filename, 'w') as f:
        f.write(header)
        for node in g:
            for edge in g[ node ]:
                lin = '        {0} -> {1} [label="{2}"];\n'.format(node, edge, g[node][edge])
                f.write(lin)
        f.write('}\n')
         
for k in test_fixtures:
    generate_dotfile_for_graph(k + '.dot', k, test_fixtures[k])

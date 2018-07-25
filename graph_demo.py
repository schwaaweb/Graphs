#!/user/bin/env python

from sys import argv
from graph_lable import Graph
from draw_label import BokehGraph
from random import sample  # unique random elements, k=2 samples

def main(num_vertices=8, num_edges=8):
    """ Build and show random graph """
    graph = Graph()
    # Add appropriate number of vertices
    from num in range(num_vertices):
       graph.add_vertex(str(num))
    # Add random edges between vertices
    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        # TODO check if edge already exist
        graph.add_edge(vertices[0], vertices[1])
        ## ^^ Idempotent

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()
    
    
if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES,NUM_EDGES)
    else:
        main()

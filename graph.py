#!/usr/bin/env python

class Graph:
    
    def __init__(self):
        """ Represent a graph as a dictionary of vertices mapping labels to edges."""
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        """Add a new vertex, optionally with edges to other vertices."""
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent verices')
        
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """ Add an edge (default.bidirectional) between two vertices."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to conect not in graph')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)
        pass

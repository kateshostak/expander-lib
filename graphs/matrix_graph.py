from abstract_graph import AbstractGraph

from numpy import (
    zeros,
    memmap,
)


class MatrixGraph(AbstractGraph):
    def __init__(self, adjacency_list):
        super(MatrixGraph, self).__init__(adjacency_list)

    def _convert_the_graph(self, file_name):
        adjancency_matrix = zeros(
            shape=self.number_of_nodes,
            dtype=('f')
        )

        adjancency_matrix_file = open(file_name, "wb")

        for row in self.adjancency_list:
            adjancency_matrix[:] = 0
            for node in row:
                adjancency_matrix[node] = 1
            adjancency_matrix.tofile(adjancency_matrix_file)

        adjancency_matrix_file.close()

        return self._get_the_pointer_of_a_file(file_name)

    def _get_the_pointer_of_a_file(self, file_name):
        return memmap(
            file_name,
            dtype='f',
            mode='r',
            shape=(
                self.number_of_nodes, 
                self.number_of_nodes
            )
        )

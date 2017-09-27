from numpy import arange, random

from abstract_expander import AbstractExpander


class RandomExpander(AbstractExpander):
    def __init__(self, size_of_group, regularity=3):
        super(RandomExpander, self).__init__(
            size_of_group,
            regularity
        )

    def generate_sets_of_nodes(self):
        return (
            random
            .permutation(
                arange(
                    self.number_of_nodes,
                    self.number_of_nodes * 2
                )
            )
        )

    def construct_the_expander(self):
        for i in xrange(self.regularity):
            permut = self.generate_sets_of_nodes()
            for j in xrange(self.number_of_nodes):
                self.adjancency_list[permut[j]][i] = j
                self.adjancency_list[j][i] = permut[j]

        return self.adjancency_list

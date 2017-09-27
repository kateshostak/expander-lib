from numpy import (
    arange,
    random,
    full,
)


class AbstractExpander(object):
    
    INSTANCE_NUMBER = -1

    def __init__(self, size_of_group, regularity):
        self.__class__.INSTANCE_NUMBER += 1
        self.regularity = regularity
        self.size_of_group = size_of_group
        self.number_of_nodes = size_of_group * size_of_group

        self.adjancency_list = full(
            shape=(self.number_of_nodes * 2, self.regularity),
            fill_value=-1,
            dtype=('int32')
        )

    def _generate_sets_of_nodes(self):
        return (
            random
            .permutation(arange(self.number_of_nodes))
            .reshape((self.size_of_group, self.size_of_group))
        )

    def construct_the_expander(self):
        raise NotImplementedError

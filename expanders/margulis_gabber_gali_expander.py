from abstract_explicit import AbstractExplicit


class MargulisGabberGaliExpander(AbstractExplicit):
    REGULARITY = 8
    def __init__(self, size_of_group):
        super(
            MargulisGabberGaliExpander,
            self
        ).__init__(
            size_of_group,
            MargulisGabberGaliExpander.REGULARITY
        )

    def _calc_adjancency_nodes(self, x0, y0, adj_node):
        if adj_node == 0:
            return (x0 + 2*y0) % self.size_of_group, y0
        elif adj_node == 1:
            return (x0 + (2*y0 + 1)) % self.size_of_group, y0
        elif adj_node == 2:
            return x0, (y0 + 2*x0) % self.size_of_group
        elif adj_node == 3:
            return x0, (y0 + (2*x0 + 1)) % self.size_of_group
        elif adj_node == 4:
            return (x0 - 2*y0) % self.size_of_group, y0
        elif adj_node == 5:
            return (x0 - (2*y0 + 1)) % self.size_of_group, y0
        elif adj_node == 6:
            return x0, (y0 - 2*x0) % self.size_of_group
        elif adj_node == 7:
            return x0, (y0 - (2*x0 + 1)) % self.size_of_group

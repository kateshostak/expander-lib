from abstract_explicit import AbstractExplicit


class MargulisExpander(AbstractExplicit):
    REGULARITY = 5
    def __init__(self, size_of_group):
        super(
            MargulisExpander,
            self
        ).__init__(
            size_of_group,
            MargulisExpander.REGULARITY
        )

    def _calc_adjancency_nodes(self, x0, y0, adj_node):
        if adj_node == 0:
            return x0, y0
        elif adj_node == 1:
            return (x0 + 1) % self.size_of_group, y0
        elif adj_node == 2:
            return x0, (y0 + 1) % self.size_of_group
        elif adj_node == 3:
            return (x0 + y0) % self.size_of_group, y0
        elif adj_node == 4:
            return -y0 % self.size_of_group, x0
from abstract_expander import AbstractExpander


class AbstractExplicit(AbstractExpander):
    def __init__(self, size_of_group, regularity):
        super(
            AbstractExplicit,
            self
        ).__init__(
            size_of_group,
            regularity
        )

    def construct_the_expander(self):
        set_of_nodes = self._generate_sets_of_nodes()

        for row in set_of_nodes:
            for node in row:
                x0 = node / self.size_of_group
                y0 = node % self.size_of_group

                for i in xrange(0, self.regularity):
                    self._connect_the_nodes(x0, y0, node, i)

        return self.adjancency_list

    def _calc_adjancency_nodes(self, x0, y0, adj_node):
        raise NotImplementedError


    def _connect_the_nodes(self, x0, y0, i, adj_node):
        x, y = self._calc_adjancency_nodes(x0, y0, adj_node)
        j = (
            x * self.size_of_group +
            y % self.size_of_group +
            self.number_of_nodes
        )
        self.adjancency_list[i][adj_node] = j
        self.adjancency_list[j][adj_node] = i
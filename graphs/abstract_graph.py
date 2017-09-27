class AbstractGraph(object):
    INSTANCE_NUMBER = -1

    def __init__(self, adjancency_list):
        AbstractGraph.INSTANCE_NUMBER += 1
        self.adjancency_list = adjancency_list
        self.number_of_nodes, self.regularity = (
            adjancency_list.shape
        )

    def get_the_graph(self, file_name=None):
        if not file_name:
            file_name = "tmpgraph"
        if not self._check_if_expander_exists():
            print "There's no expander constructed yet"
            return None
        else:
            return self._convert_the_graph(file_name)

    def _generate_file_name(self):
        return (
            self.__class__.__name__ +
            str(self.__class__.INSTANCE_NUMBER)
        )

    def _check_if_expander_exists(self):
        return (
            -1 not in self.adjancency_list and
            len(self.adjancency_list)
        )

    def _convert_the_graph(self, file_name):
        raise NotImplementedError

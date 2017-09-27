from __future__ import print_function

import expanders
import graphs
import expansion_constant as expconst


class TestExpanders(object):

    EXPANDER_NAMES = [
        "MargulisExpander",
        "MargulisGabberGaliExpander",
        "AngluinExpander",
        "RandomExpander"
    ]

    def __init__(self, number_of_tests=0, size_of_zn=[]):
        self.size_of_zn = size_of_zn
        self.number_of_tests = number_of_tests

    def run_analysis(self):
        analysis = open("analysis", "wb")
        for n in self.size_of_zn:
            expander_list = self._create_expanders(n)
            print(n, file=analysis)
            for expander in expander_list:
                exp_const_avrg = 0
                print(
                    expander.__class__.__name__, 
                    file=analysis, end=' '
                )

                for i in xrange(0, self.number_of_tests):
                    exp_const_avrg += (
                        self._calc_exp_const(expander)
                )

                print(
                    exp_const_avrg/self.number_of_tests, 
                    file=analysis
                )

    def _create_expanders(self, size_of_zn):
        expander_list = map(
            lambda name: getattr(expanders, name)(size_of_zn),
            TesExpanders.EXPANDER_NAMES
        )
        return expander_list

    def _calculate_expansion_constant(self, expander):
        adj_list_of_expander = expander.construct_expander()
        adj_matrix_of_expander = (
            graphs.
            MatrixGraph(adj_list_of_expander).get_the_graph()
        )
        expansion_constant = expconst.calculate_exp_const(
            adj_matrix_of_expander, 
            expander.regularity
        )
        
        return expansion_constant


number_of_tests = 50
size_of_zn = [2, 4, 8, 10, 14, 18, 20, 30]
TesExpanders(number_of_tests, size_of_zn).run_analysis()

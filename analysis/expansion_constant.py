from math import sqrt

from scipy.sparse.linalg import eigsh


def calc_secnd_most_eigenvalue(adjancency_matrix):
    if adjancency_matrix is not None:
        evals_large, evecs_large = eigsh(
            adjancency_matrix, 2, which='LM'
        )
        return evals_large[1]
    else:
        return None


def calculate_exp_const(adjancency_matrix, regularity):
    second_largest_eigenavlue = (
        calc_secnd_most_eigenvalue(adjancency_matrix)
    )
    
    if second_largest_eigenavlue is not None:
        return (
            2 * sqrt(regularity) -
            second_largest_eigenavlue
        )
    else:
        print "No eigenvalue for an empty expander"
        return None
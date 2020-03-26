from fractions import Fraction as Fr
import numpy as np


def get_bernoulli(num):
    A = [0] * (num + 1)
    for m in range(num + 1):
        A[m] = Fr(1, m + 1)
        for j in range(m, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j])
    return float(A[0])  # (which is Bn)


number = int(input())
bernoulli_number = get_bernoulli(number)
if bernoulli_number < 0:
    bernoulli_number = -number
natural_logarithm_number = np.log(bernoulli_number)
print(natural_logarithm_number)

#A
import numpy as np

def vandermonde(N):
    vec = np.arange(N) + 1  
    vander_matrix = vec ** np.arange(N).reshape(N, 1) 
    return vander_matrix
vander = vandermonde(12)
print("Ma trận Vandermonde (12x12):\n", vander)

#B
x = np.ones(12)
b = vander @ x
print("\nVector b sau khi nhân ma trận Vandermonde với vector x:\n", b)

#C
import numpy.linalg as la

vander_inv = la.inv(vander)
x_naive = vander_inv @ b
print("\nKết quả giải hệ phương trình bằng cách nghịch đảo ma trận:\n", x_naive)

#D
x_solve = la.solve(vander, b)
print("\nKết quả giải hệ phương trình bằng solve:\n", x_solve)
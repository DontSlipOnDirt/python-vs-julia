import time
from julia import Main as jl
import numpy as np

jl.include("julia_functions.jl")

def test_matrix_mult_benchmark():

    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)

    jl.A = A
    jl.B = B

    jl_time = jl.matrix_mult_benchmark(jl.A, jl.B)

    # python calculations
    start = time.time()
    C = np.matmul(A, B)
    end = time.time()

    py_time = (end - start)*1000

    return jl_time, py_time

# -- testing --
jl_time, py_time = test_matrix_mult_benchmark()

print("Julia Time:", jl_time, "ms")
print("Python Time:", py_time, "ms")
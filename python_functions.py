import torch
import time
import numpy as np

# Create large random matrices
A = np.random.rand(10000, 10000)
B = np.random.rand(10000, 10000)

# Benchmark matrix multiplication
start = time.time()
C = np.matmul(A, B)  # or A @ B
end = time.time()

print("Python (NumPy) Matrix Multiplication Time:", (end - start)*1000, "ms")

# Create large array
X = np.random.rand(1000000)

# Benchmark element-wise exponential function
start = time.time()
Y = np.exp(X)
end = time.time()

print("Python (NumPy) Element-wise Exp Time:", (end - start)*1000, "ms")

# Define function
def f(x):
    return x**3 + 2*x**2 + 5*x

# Create input tensor with gradients enabled
x = torch.linspace(-100, 100, 100000, requires_grad=True)

# Benchmark gradient computation
start = time.time()
y = f(x)
y.sum().backward()  # Compute gradient
end = time.time()

print("Python (PyTorch) Gradient Computation Time:", (end - start)*1000, "ms")

import numpy as np

A = np.array([[0.76, -0.01, -0.14, -0.16],
              [-0.01, 0.88, -0.03, 0.06],
              [-0.14, -0.03, 1.01, -0.12],
              [-0.16, 0.06, -0.12, 0.72]])

b = np.array([0.68, 1.18, 0.12, 0.74])
n = len(b)

x_last = np.array([1.0, 1.0, 1.0, 1.0])
x_next = np.array([1.0, 1.0, 1.0, 1.0])
error = 10.0
K = 0

while error > 1e-6:
    for i in range(n):
        indices = list(range(0, i)) + list(range(i + 1, n))
        x_next[i] = (b[i] - np.sum(A[i, indices] * x_last[indices])) / A[i, i]

    error = np.max(np.abs((x_next - x_last) / x_last))
    x_last = x_next.copy()
    K += 1

print(f"Iterations: {K}")
print(f"Results: {x_next}")
print(f"Errors: {error}")
import numpy as np

def func_fixed(x):
    return (np.sin(x) - 5) / 6

def func(x):
    return 6 * x + 5 - np.sin(x)

def fixed_point_iter(func, point, maxiter=10):
    
    for i in range(maxiter):
        print(point)
        point = func(point)

    return point

solution = fixed_point_iter(func_fixed, -2)

print("Fixed Point is:", solution)
print("f(solution) =", func(solution))


# Write your code here
from copy import copy

def rotate(xs, n):
    xs2 = copy(xs)
    return xs[n:] + xs2[:n]

print(rotate([1, 2, 3], 2))


#oplossing
# def rotate(xs, n):
#     for _ in range(n):
#         x = xs.pop(0)
#         xs.append(x)

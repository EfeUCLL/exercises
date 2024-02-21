# Write your code here

def rotate(xs, n):
    return xs[n:] + xs[:n]

print(rotate([1, 2, 3], 2))


#oplossing
# def rotate(xs, n):
#     for _ in range(n):
#         x = xs.pop(0)
#         xs.append(x)

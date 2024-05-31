# Write your code here

def is_increasing(ns):
    ms = ns[1:]
    paired = list(zip(ns, ms))

    for j in range(len(paired)):
        if paired[j][0] > paired[j][1]:
            return False
    return True

# oplossing:
# def is_increasing(ns):
#     for (x, y) in zip(ns, ns[1:]):
#         if x > y:
#             return False
#     return True
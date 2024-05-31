# Write your code here

def is_increasing(ns):
    ms = ns[1:]
    paired = list(zip(ns, ms))

    if len(ns) == 0 or len(ns) == 1:
        return True

    i = len(paired)
    while i > 0:
        for j in range(len(paired)):
            if paired[j][0] <= paired[j][1]:
                i -= 1
            else:
                return False
        return True

# oplossing:
# def is_increasing(ns):
#     for (x, y) in zip(ns, ns[1:]):
#         if x > y:
#             return False
#     return True
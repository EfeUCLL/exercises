# Write your code here

def target_sum(ns, target):
    for i in range(len(ns)):
        for j in range(i, len(ns)):
            if ns[i] + ns[j] == target:
                return True
    return False

#oplossing
# def target_sum(ns, target):
#     for x in ns:
#         for y in ns:
#             if x + y == target:
#                 return True
#     return False

# Write your code here

def median(ns):
    sorted_list = sorted(ns)
    if len(sorted_list) == 1:
        return sorted_list[0]
    
    elif len(sorted_list) == 2:
        return (sorted_list[0] + sorted_list[1]) / 2
    
    elif len(sorted_list) % 2 == 0:
        index_left = (len(sorted_list) // 2) - 1
        index_right = index_left + 1

        return (sorted_list[index_left] + sorted_list[index_right]) / 2

    return sorted_list[len(sorted_list) // 2]

#oplossing
# def median(ns):
#     sorted_ns = sorted(ns)
#     i = len(sorted_ns) // 2

#     if len(sorted_ns) % 2 == 0:
#         return (sorted_ns[i - 1] + sorted_ns[i]) / 2
#     else:
#         return sorted_ns[i]
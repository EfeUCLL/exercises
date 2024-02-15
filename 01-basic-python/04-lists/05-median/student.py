# Write your code here

def median(ns):
    sortedList = sorted(ns)
    if len(sortedList) == 1:
        return sortedList[0]
    
    elif len(sortedList) == 2:
        return (sortedList[0] + sortedList[1]) / 2 
    
    elif len(sortedList) % 2 == 0:
        indexLeft = (len(sortedList) // 2) - 1
        indexRight = indexLeft + 1

        median = (sortedList[indexLeft] + sortedList[indexRight]) / 2
        return median
    
    median = sortedList[len(sortedList) // 2]
    return median

#oplossing
# def median(ns):
#     sorted_ns = sorted(ns)
#     i = len(sorted_ns) // 2

#     if len(sorted_ns) % 2 == 0:
#         return (sorted_ns[i - 1] + sorted_ns[i]) / 2
#     else:
#         return sorted_ns[i]
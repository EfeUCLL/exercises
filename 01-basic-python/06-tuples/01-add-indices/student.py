# Write your code here

def add_indices(xs):
    index_list = []
    for i in range(len(xs)):
        index_list.append(i)

    return list(zip(index_list, xs))

# solution:
# def add_indices(xs):
#     indices = range(len(xs))
#     return list(zip(indices, xs))
#
# # Better: relying on existing functionality
# def add_indices(xs):
#     return list(enumerate(xs))

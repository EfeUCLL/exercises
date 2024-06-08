def indices_of(xs, condition):
    indices = []
    for element in xs:
        if condition(element):
            indices.append(xs.index(element))
    return indices

# oplossing
# def indices_of(xs, condition):
#     return [index for index in range(len(xs)) if condition(xs[index])]

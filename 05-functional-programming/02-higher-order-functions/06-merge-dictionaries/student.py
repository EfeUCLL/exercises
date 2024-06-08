def merge_dictionaries(dict1, dict2, merge_function):
    result = dict1
    for key, value in dict2.items():
        if key in result:
            result[key] = merge_function(result[key], value)
        else:
            result[key] = value
    return result

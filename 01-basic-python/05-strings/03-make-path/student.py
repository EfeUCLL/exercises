# Write your code here

def make_path(parts):
    string = ""
    for i in range(len(parts)):
        string += parts[i]
        if i != len(parts) - 1:
            string += "/"
    return string


# oplossing:
# def make_path(parts):
#    return "/".join(parts)

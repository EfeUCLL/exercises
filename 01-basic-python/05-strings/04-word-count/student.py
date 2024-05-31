# Write your code here

def word_count(string):
    amount = 1

    if len(string) == 0:
        return 0

    for i in range(len(string)):
        if string[i] == " ":
            amount += 1
    return amount

# oplossing:
# def word_count(string):
#     if len(string) != 0:
#         return len(string.split(' '))
#     else:
#         # Separate logic necessary for empty string because "".split(' ') yields ['']
#         return 0


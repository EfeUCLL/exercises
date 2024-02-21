# Write your code here

def format_time(hours, minutes, seconds):
    return f'{"0" + str(hours) if hours < 10 else "" + str(hours)}:{"0" + str(minutes) if minutes < 10 else "" + str(minutes)}:{"0" + str(seconds) if seconds < 10 else "" + str(seconds)}'

#oplossing
# def format_time(hours, minutes, seconds):
#     def format(x):
#         return str(x).rjust(2, '0')

#     hours = format(hours)
#     minutes = format(minutes)
#     seconds = format(seconds)

#     return f"{hours}:{minutes}:{seconds}"

# The active selection rjust is a built-in Python method for string objects. It's used to right-align a string by padding it with a specified character (default is a space) on the left side.

# The rjust method takes two parameters:

# width: The width of the resulting string. If it's less than the length of the original string, the original string is returned as is.
# fillchar (optional): The character used for padding. If it's not provided, a space character is used.
# Here's an example of how to use rjust:

# s = "hello"
# print(s.rjust(10, '-'))  # Output: "-----hello"
# class AssocList:
#     def __init__(self):
#         self.__items = []
#
#     def __getitem__(self, key):
#         for item in self.__items:
#             if item[0] == key:
#                 return item[1]
#             else:
#                 raise KeyError()
#
#     def __setitem__(self, key, value):
#         for item in self.__items:
#             if item[0] != key:
#                 self.__items.append([key, value])
#             else:
#                 item[1] = value
#
#     def __contains__(self, key):
#         for item in self.__items:
#             if item[0] == key:
#                 return True
#         return False
#
#     def __len__(self):
#         return len(self.__items)
#
#     def keys(self):
#         keys = []
#         for item in self.__items:
#             keys.append(item[0])
#         return keys
#
#     def values(self):
#         values = []
#         for item in self.__items:
#             values.append(item[1])
#         return values

#Opnieuw maken nadat OO gedaan is!!!
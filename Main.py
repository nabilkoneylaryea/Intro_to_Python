# WHILE-LOOPS
#
# ! using break statements !
# ! using enumerate(list_name) returns tuples of indexes and list items in pairs!
#
# EXAMPLE:
# from random import randint
# truth_condition = True
# i = 0
# list = [randint(1,100) for num in range(1000)]
# while truth_condition:
#     if list[i] == 25:
#         print('25 found at index', i)
#     i += 1
#     if i >= len(list):
#         truth_condition = False
#
# ZIP GENERATOR:
#
# returned as an object swo must cast to list to do stuff with it
# combines lists into list of tuple pairs based on indexes of items in original lists
# EXAMPLE:
# first_names = ['spongebob', 'squidward', 'patrick']
# last_names = ['squarepants', 'tentacles', 'star']
# names = list(zip(first_names, last_names))
# print(names)

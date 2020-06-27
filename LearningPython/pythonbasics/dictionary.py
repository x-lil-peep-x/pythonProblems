dictionary = {
    'pen': [1, 2, 3],
    'apples': 'hello',
    'age': 20
}
# Another way to instance a dictionary
# dictionary2 = dict(name='Erick')
# print(dictionary2)
# my_list = [
#     {
#         'a': [1, 2, 3],
#         'b': 'hello',
#         'c': True
#     },
#     {
#         'a': [1, 2, 3],
#         'b': 'hello',
#         123: True
#     }
# ]
#
# print(my_list[0]['a'][1])
# print(dictionary['a'][0])
# print(my_list[1][123])

# METHODS
print(dictionary.get('age', 55))
print('age' in dictionary.keys())
print(20 in dictionary.values())

print(20 in dictionary.keys())
print('age' in dictionary.values())

print(20 in dictionary.items())


print(dictionary)
dictionary['apples'] = 44
dictionary.update({'pen': 'pencil'})
print(dictionary)
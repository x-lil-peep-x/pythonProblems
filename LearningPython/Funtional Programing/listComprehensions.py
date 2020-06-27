# LIst
my_nums = [num ** 2 for num in range(1, 101)]
my_chars = [char for char in 'You are dog shit !']
even_numbers = [num ** 2 for num in range(1, 101) if num % 2 == 0]

print(my_nums)
print(my_chars)
print(even_numbers)

# Set Comprenhension
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {'shit': 3}
my_dict.update({key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0})
another_dict = {num: num * 2 for num in [1, 2, 3]}
print(my_dict)
print(another_dict)

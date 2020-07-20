

# def make_list(num):
#     result = []
#     for index in range(num):
#         result.append(index*2)
#     return result
#

def generator_function(max_num):
    for num in range(max_num):
        # yield convert our func in a generator
        yield num

g = generator_function(100)
next(g)
next(g)
print(next(g))
#
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        time1 = time()
        result = fn(*args, **kwargs)
        time2 = time()
        print(f'Took {time2 - time1} s')
        return result

    return wrapper


@performance
def long_time():
    print('1')
    for num in range(1000000):
        num * 5

@performance
def long_time2():
    print('2')
    for num in list(range(1000000)):
        num * 5


long_time()
long_time2()

#to create a generator
def gen_fun(size):
    for num in range(size):
        yield num


for item in gen_fun(100):
    print(item)
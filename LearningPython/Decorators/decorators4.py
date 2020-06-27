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
    for index in range(100000000000):
        index * 5

long_time()
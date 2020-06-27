# decorator
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print(args, kwargs)
        print('*********')
        func(*args, **kwargs)
        print('*********')

    return wrap_func


@my_decorator
def hello(greeting, emoji ='=c',*args ,**kwargs):
    print(greeting, emoji)



hello('Shit', '=D')
hello('Shit', emoji='shit',name='Shit')
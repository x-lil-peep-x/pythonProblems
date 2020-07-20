while (True):
    try:
        age = int(input('What is your age? '))
        print(10/age)
        raise ValueError('Hey cut it out')
    # if there is an error
    except ZeroDivisionError:
        print('Please enter a higher than 0')
        break
    # if there is no error
    else:
        print('No error')
    finally:
        print('Ok i am done')
    print('Can you see me?')
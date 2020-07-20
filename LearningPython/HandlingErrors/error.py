while (True):
    try:
        age = int(input('What is your age? '))
        print(10/age)
    # if there is an error
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a higher than 0')
    # if there is no error
    else:
        print('No error')
        break
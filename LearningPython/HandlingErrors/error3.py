while (True):
    try:
        age = int(input('What is your age? '))
        print(10/age)
    # if there is an error
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter a higher than 0')
        break
    # if there is no error
    else:
        print('No error')
    finally:
        print('Ok i am done')
    print('Can you see me?')
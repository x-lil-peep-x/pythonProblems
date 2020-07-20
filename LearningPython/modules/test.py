import utility
# from LearningPython.modules import utility
# be explicit with the modules
from LearningPython.modules.utility import divide_numbers, multiply, student
import LearningPython.modules.shopping.other.shopping as shopping
from LearningPython.modules.shopping.other.shopping import buy

print(__name__)
print(utility.divide_numbers(3, 2))
print(shopping)
print(shopping.buy('apples'))
print(buy('pear'))
print(multiply(3, 3))

if __name__ == '__main__':
    print('Please run this')
    print(type(student))




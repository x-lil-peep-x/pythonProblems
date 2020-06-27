# letters = ['a', 'b', 'c', 'z', 'd', 'e', 'a']
# new_letters = letters.copy()
# letters.sort()
# print(new_letters)
# print(letters)
# print(letters.count('a'))
# print('e' in letters)
# print('1' in '123')
# # Problem
# birth_year = int(input('What year were you born ?'))
# age = 2020 - birth_year
# print(f'Your age is {age} !')
# letters.sort()
# print(sorted(letters))
letters = ['a', 'b', 'c', 'z', 'd', 'e', 'a']
letters.sort()
letters.reverse()
# print(letters[::-1])
# print(letters)
print(list(range(20)))
newSentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJo'])
print(newSentence)
# List unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)

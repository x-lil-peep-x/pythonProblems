chars = ['a', 'b', 'c', 'd', 'e', 'a', 'b']
duplicates = list({char for char in chars if chars.count(char) > 1})
print(duplicates)
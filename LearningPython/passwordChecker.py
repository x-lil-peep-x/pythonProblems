# input('jay jay')
# input('secret')
# print('{username}', your password {******} is {long} letters long)')
username = input('''What's your username?''')
password = input('''What's your password?''')
password_length = len(password)
hidden_password = '*' * password_length
print(f'{username}, your password ,{hidden_password}, is {len(password)}, letters long')

is_old = True
is_licenced = True
# Truthy and falsy
username = 'erick'
# ask if exists
if username:
    print(f'username exists and is {username}')
password = ''
if password:
    print(f'Your password is {password}')
else:
    print('Password no exists')


if is_old and is_licenced:
    print('You are old enough to drive, and you have a licence !')
elif is_old:
    print('You are old enough to drive !')
elif is_licenced:
    print('You have a licence !')
else:
    print('You can not drive !')

print('Ok ok')

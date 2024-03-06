# bytearray

user_info = bytearray(' ', 'utf-8')

name = input('Isim: ')
lastname = input('Familiya: ')
age = input('Yosh: ')

user_info.extend(bytes(name, 'utf-8'))
user_info.extend(bytes(lastname, 'utf-8'))
user_info.extend(bytes(age, 'utf-8'))
print(user_info)
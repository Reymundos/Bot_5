# bytearray

us_infos = bytearray(' ', 'utf-8')

name = input("Ism: ")
lastname = input("Familiya: ")
age = input("Yosh: ")

us_infos.extend(bytearray(name, 'utf-8'))
us_infos.extend(bytearray(lastname, 'utf-8'))
us_infos.extend(bytearray(age, 'utf-8'))

print(us_infos)

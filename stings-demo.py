website = "https://nursimaoner.com"
course = "Python Kursu"

#1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)
length = len(website)

#2- 'website' içinden www karakterlerini alın.
result = website[7:10]

#3-'website' içinden com karaktrlerini alın.
result = website[22:25]
result = website [length-3:length]
#4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]
result = course[:15]
result = course[-15:]
#5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]

name, surname, age, job = 'Nursima', 'ÖNER',22, 'mühendis'

#6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Nursima ÖNER, Yaiım 22 ve mesleğim mühendis.'

result = "Benim adım "+ name+ " "+surname+ "Yaşım "+ age+ "mesleğim "+ job
result = "Benim adım {0}{1}, Yaşım{2} ve mesleğim {3}".format(name,surname,age)
result = f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}'

#7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s= 'Hello world'
s = s[0:6] + 'W' + s[-4:]
s.replace('w','W')
print(s)

#8- 'abc' ifadesini yan yana 3 defa yazdırın.

result = 'abc' *3
print(result)
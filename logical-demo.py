# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

sayi = float(input('sayı: '))
result = (sayi > 0) and (sayi <= 100)

print(f'sayı 0-100 arasında mı: {result}')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))
result = (sayi > 0) and (sayi % 2 == 0)

print(f'girilen sayı pozitif çift sayı mı: {result}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'email@nursimaoner.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('password: ')

result = (girilenEmail == email) and (girilenPassword == password)
print(f'uygulamaya giriş başarılı mı: {result}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result = (a > b) and (a > c)
print(f'a en büyük sayıdır : {result}')

result = (b > a) and (b > c)
print(f'b en büyük sayıdır : {result}')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.


vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final : '))

ortalama = ((vize1 + vize2) / 2) * 0.6 + (final * 0.4)

# a şıkkı için mantık: (ortalama >= 50) and (final >= 50)
# b şıkkı dahil edilmiş son hali:
result = (ortalama >= 50) or (final >= 70)

print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: {result}')

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = int(input('boyunuz: ')) 


index = (kg) / ((hg / 100) ** 2)

# Grupları mantıksal operatörlerle belirleyelim
Zayif = (index >= 0) and (index <= 18.4)
Normal = (index > 18.4) and (index <= 24.9)
Kilolu = (index > 24.9) and (index <= 29.9)
Obez = (index > 29.9) and (index <= 34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {Zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {Normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {Kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {Obez}')

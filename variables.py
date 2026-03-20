maasAli = 50000
maasAhmet = 40000
vergi = 0.5

print(maasAli- (maasAli*vergi))
print(maasAhmet - (maasAhmet*vergi))

#Değişken Tanımlama Kuralları
#rakam ile başlayamaz

number1 = 10
print(number1)

number2 = 20
print(number2) = 20

number1 += 30
print(number1)


#Büyük Küçük Harf Duyarlılığı

age = 20
AGE = 30

print(age)
print(AGE)

#Türkçe karakter kullanmayalım

x = 1                 #int
y = 2.3               #float
name = "Nursima"      #string
isStudent = True      #bool

x, y, name, isStudent = (1,2.3,"NUR", True)

a = '10'
b = '20'
print(a+b) #30 =>1020

firstName = "Nursima"
lastName = "ÖNER"
print(firstName+lastName) # Nursima ÖNER
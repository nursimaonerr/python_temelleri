'''
Daire Alanı: πr^2
Daire Çevresi : 2πr
Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız.(r: 3.14)
'''

pi = 3.14
r = float(input("yarıçap: "))

alan = pi * (r**2)
print(type(alan))

cevre = 2 * pi * r
print(" alan: "+ str(alan)+ " çevre: "+ str(cevre))

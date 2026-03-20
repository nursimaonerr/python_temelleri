# x = 5
# y = 16
# z = 20

x, y, z = 5, 16, 20

#x,y = y,x
x += 5     # x = x + 5 (Topla ve ata)
x -= 5     # x = x - 5 (Çıkar ve ata)
x *= 5     # x = x * 5 (Çarp ve ata)
x /= 5     # x = x / 5 (Böl ve ata)
x %= 5     # x = x % 5 (Kalanı/Modu al ve ata)
y //= 5    # y = y // 5 (Tam böl ve ata)
y **= z    # y = y ** z (üs al ve ata)
print(x, y, z)

values = 1, 2, 3, 4, 5

print(values)
print(type(values))

x, y, *z = values
print(x, y, z[1])
# username, password => database
# 'nursimaoner' , '123456'

a, b, c, d = 5, 5, 10, 4
password = '1234'
username = 'nursimaoner'

result = ( a==b ) # True
result = (a ==c ) # False
result = ('nrsm' == username)
result = ('nursimaoner' == username)
result = (a != b)  # False (5, 5'e eşit değildir ifadesi yanlıştır)
result = (a != c)  # True  (5, 10'a eşit değildir ifadesi doğrudur)
result = (a > c)   # False (5, 10'dan büyüktür ifadesi yanlıştır)
result = (a < c)
result = (a >= b)  # True (5, 5'ten büyük veya eşittir ifadesi doğrudur)
result = (c <= b)  # False (10, 5'ten küçük veya eşittir ifadesi yanlıştır)
result = (True == 1)
result = (False == 0)
result = (False +True +40)
p=23# известное число
g=18 # известное число число

a=5 # закрытый ключ Алисы
b=8 # закртый ключ Боба

aliceSends = (g**a)%p # вычисляется открытый ключ
bobSends = (g**b)%p # вычисляется открытый ключ

aliceComputes = (bobSends**a)%p # общий секретный ключ
bobComputes = (aliceSends**b) %p # общий секретный ключ

print ("Alice sends    ", aliceSends )
print ("Bob sends      ", bobSends)
print ("Alice computes ", aliceComputes)
print ("Bob computes   ", bobComputes )

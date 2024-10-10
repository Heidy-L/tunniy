"""Matemaatilised tehted"""
import math

# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b

# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
a = float(input("Sisesta külg a:"))
b = float(input("Sisesta külg b:"))
c = float(math.sqrt(a ** 2 + b ** 2))
p = print (a + b + c)
s = print ( a * b / 2)



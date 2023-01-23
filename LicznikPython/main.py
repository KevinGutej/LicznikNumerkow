print("Give me number:")
input = input()
lista = map(int,list(str(input)))
licznik = 0
for i in lista:
    licznik = licznik + i

print("Your sum is: %s" % licznik)
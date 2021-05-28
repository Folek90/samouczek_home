

# SEKCJA 4 FUNKCJE PRINT: 

# Cwiczenie 1:

print('Ucz sie pythona!')

# Cwiczenie 2:

age = 20

print('Mam', age, 'lat.')

print(f'Mam {age} lat.')

print('Mam ' + str(age) + ' lat.')

# Cwiczenie 3

lang = 'Python'
version = '3.8'

print(f'Ucze sie jezyka {lang} w wersji {version}')

print('Ucze sie jezyka {} w wersji {}'.format(lang, version))


# Cwiczenie 6

price = 34.99
weight = 10

print(f'Cena: {price} zl. Waga: {weight} kg')

# Cwiczenie 7

pi = 3.1415926535

print(f'Przyblizenie liczby pi: {pi:.2f}')


# Cwiczenie 8

print('-' * 40)
print('WERSJA: 1.0.1')
print('-' * 40)

# Cwiczenie 10

print('summer', 'time', 'holiday', sep='#')

# Cwiczenie 11

import math

radius = 5

area = pi * radius **2

print('Pole kola wynosi', pi*radius**2)

print(f'Pole kola wynosi {area:.2f} cm2')


# ______________________________________________    sekcja 5:    OBLICZENIA W PYTHONIE:       __________________________________________

# Cwiczenie 12

pv = 1000

r = 0.03
n = 5

fv = pv * (1 + r)**n

print(f'Wartosc koncowa inwestycji wynosi: {fv:.2f} PLN')


# Cwiczenie 14



a1 = 14
a10 = 50
n = 10

s10 = ((a1 + a10) / 2) * n

print(f'Suma pierwszych 10 wyrazow ciagu wynosi: {s10}')


# Cwiczenie 17
# Wyznacz srodek odcinka o koncach w punktach: A = (2, 4) , B = (-4, 6)


a1 = 2
a2 = 4

b1 = -4
b2 = 6

odc_A = (a1 + b1) / 2
odc_B = (a2 + b2) / 2

print(f' Srodek odcinka A wynosi {odc_A}, natomiast odcinka B wynosi {odc_B}')


# Cwiczenie 20:
# Oblicz srednia geometryczna z liczb: 4, 3, 4.5, 5.

x1, x2, x3, x4 = 4, 3, 4.5, 5

geo = (x1 * x2 * x3 * x4)**(1/4)

print(f'Srednia geometryczna podanych liczb wynosi {geo:.2f}')


# ________________________________________ Sekcja 6 OPERATOR WYCINANIA: ______________________________________

# Cwiczenie 23:
# Z podanej nazwy pliku wytnij jego rozszerzenie. Wynik wydrukuj do konsoli.

filename = 'viev.jpg'

print(filename[5:])
print()
print(filename[-3:])

# Cwiczenie 24:
# Z podanego tekstu wytnij kod sklejajacy 3 peirwsze litery i trzy ostatnie znaki. Wynik wydrukuj do konsoli. 

text = 'PKV-89415-PLN'

print(text[:3] + text[-3:])


# Cwiczenie 25:
# Z podanego tekstu usun spacje. Nastepnie otrzymany wynik '100101' przedstaw w zapisie dziesietnym. Wydrukuj liczbe do konsoli.

string = '1 0 0 1 0 1'

binary = string[::2]
number = int(binary, 2)
print(f'Znaleziona liczba: {number}')

# Cwiczenie 26:
# Poslugujac sie operatorem wycinania, odwroc kolejnosc znakow w ponizszym tekscie: 

text = 'Kurs Python'
print(text[::-1])



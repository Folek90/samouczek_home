'''
print('witajcie!')

list = range(10)
print(list)

for i in range(20):
    print('siemanko!')

abc = input('podaj imie: ')
print('Twoje imie to ' + abc)

for i in range(10):
    print('niech zyje wolnosc')
'''
'''
print(2 + 2.4)

print(12 != 12)

print(2 == 2)


x = 10 + 45*2

if x == 10:
    print('x jest równe 10!')
elif x == 100:
    print('x jest rowny sto!')
else:
    print('x jest rozny')

print()

osoba = 'Piotr Kowalski' # lista znakow, TEKST ( list )
for x in osoba:
    print(x)

wspinaczki = ['skałkowa', 'górska', 'miejska'] # LISTA ( list )
for x in wspinaczki:
    print(x)
print()

obiektywy = ( 'waski', 'szeroki', 'makro')  # KROTKA ( tuple )
for x in obiektywy:
    print (x)
print()

tance = { 'klasyczy', 'ludowy', 'wspolczesny'}  # ZBOIRY ( sety )
for x in tance:
    print(x)


# ======================================== ROZDZIAL 3 ========================================
'''
'''
# 2.
print()

zmienna = 1

if zmienna >= 10:
    print('zmienna jest wieksza lub rowna 10 !')
else:
    print('zmienna jest mniejsza niz 10 ! ')
print()

# 4
print(100 % 13) 
# 5 
print(100 // 13) 
# 6
'''
'''
age = int(input('podaj prosze swoj wiek: '))

if age > 60:
    print('Witam Cie w klubie emerytow ;)')
elif age < 60:
    print('Wciaz nie jestes emerytem, wiec korzystaj z zycia ile sie da!')
else:
    print('Do setki pozostalo Ci az 40 lat ;) !')
print()
''' 
# ===================================== ROZDZIAL 4 ===============================================
print()
'''
def funkcja(x):
    return x * 5

z = funkcja(251)

if z == 250:
    print('z jest rowne 250 ! ')
elif z < 250:
    print('z jest mniejsze od 250 ! ')
else:
    print('z jest wieksze od 250 !')

print()
'''
def funkcja_bez_parametru():
    return 2 * 3

result = funkcja_bez_parametru()
print(result)
print()
'''
# Gdy funkcja ma pobierac wiecej niz jeden parametr, wypisujemy je po przecinku.

def Funkcja_kilka_parametrow(x, y, z):
    return x + y - z

result = Funkcja_kilka_parametrow(2, 5, 3)
print(result)
print()

def kilka_parametrow(a, b, c, d):
    return a * b - c + d

result = kilka_parametrow(22, 2, 4, 5)
print(result)


def kolejny_przyklad_funkcji(g, f, s):
    return g**3 + f - s

result = kolejny_przyklad_funkcji(11, 10, 20)
print(result)
print()

# FUNKCJE WBUDOWANE: 

print(len(' ciekawe ile tu wyniesie liczba znakow'))
print(len('funkcja len, to funkcja, ktora liczy i zwraca dlugosc obiektu-lancucha znakow'))

print(str(100))
print(str(2495.22)) #zwraca nowy obiekt, konwertuje na lancuch znakow')

print(int(200000.22), ' zwracanie liczb calkowitych')  # tylko liczby calkowite zwraca.

print(float(770)) # pobiera i zwraca nowy obiekt z dokladnoscia dziesietna.

# FUNKCJA INPUT ( POBIERANIE DANYCH OD UZYTKOWNIKA )


age = input('Prosze podaj ile masz lat: ')
int_age = int(age)


if int_age == 22:
    print('jestes calkiem ok')
elif int_age < 21:
    print('jestes bardzo mlody jeszcze !')
else:
    print('szykuj sie na cmentarz! ;)')

# STOSUJEMY FUNKCJE "DEF" TEZ JAKO HERMETYZOWANIE LOGIKI:

def even_odd(x):
    if x % 2 == 0:
        print('Liczba x jest parzysta! :)')
    else:
        print('Liczba x jest nieparzysta! ')

even_odd(601)
print(even_odd)
print()


n = input('please entry a number: ')
n = int(n)

if n % 2 == 0:
    print('Liczba parzysta! :) ')
else:
    print('Zonk! Liczba niepatrzysta ;) ')


# SKRÓCENIE I UPROSZCZENIE KODU GDY CHCEMY KILKA RAZY POWTORZYC TE FUNKCJE: (brak wartosci w nawiasie)

def even_odd(): 
    n = input('please entry a some number: ')
    n = int(n)

    if n % 2 == 0:
        print('The number is even! :) ')
    else:
        print('The number is odd! ;) ')

even_odd()
even_odd()
even_odd()

# PARAMETRTY OPCJONALNE ( NIEWYMAGANE BY PODAC PRZEZ UZYTKOWNIKA)

def f(x=2):
    return x**x

print(f())
print(f(5))

def add_it(x, y=10):
    return x + y

result = add_it(4) 
print(result)

x = 97
y = 2
z = 3 

def f():
    print(x)
    print(y)
    print(z)


f()



# global:_______________________________

def f():
    global x
    x += 1
    print(x)

f()

print('======================')
def kk():
    if x <= 100:
        print('X mniejszy od 100 lub rowny 100')
    else:
        print('X wiekszy od 100')
kk()


try:

    a = input('podaj liczbe: ')
    b = input('wpisz druga liczbe: ')

    a = int(a)
    b = int(b) 

    print('wynik dzielenia to: ', a / b )
except (ZeroDivisionError, ValueError):    # GDY WYSTAPI JEDEN Z TYCH BLEDOW TO ZAMIAST KOMUNIKATU, BEDZIE NOTKA KTORA JEST WPISANA W NAWIAS PONIZEJ.
    print('=wprowadziles bledne dane!=  ')

'''
'''
print('===================================================')
# ZADANIA ROZDZIAL 4/68 str :

# ZADANIE 1

def funkcja(x):
    return x**2



print(funkcja(4))

# Zadanie 2:
def print_string(string):
    print(string)

print_string('raz, dwa i trzy')

# Zadanie 3:

def funk(x, y, a = 5, b = 10, c = 15):
    return x + y + a + b - c

result = funk(10, 20)

print(result)

# ZADANIE 4: 

def samouczek(x=20):
    return x / 2

wynik = samouczek()
print(wynik)

def samouczek_2(y = wynik):
    return y * 4

result2 = samouczek_2()
print(result2)
    
# ODPOWIEDZ Z KSIAZKI PONIZEJ, KROCEJ ZAPISANA:

def divide(x):
    return x / 2


def multiply(x):
    return x * 4

y = divide(4)
z = multiply(y)

print(z)

# Zadanie 5:
try:
    num1 = input('Prosze podaj dowolna liczbe: ')
    num2 = input('Prosze podac druga liczbe: ')

    num1 = float(num1)
    num2 = float(num2)

    print('Wynik dodawania to:', num1 + num2)
except ValueError:
    print('\n*** Zostala wprowadzona niepoprawna wartosc,\nwpisuj prosze same liczby. ***\n')

# zadanie dodatkowe:


name = input('podaj imie: ')
age = int(input('podaj swoj wiek: '))

def print_age(name, age):
    print('Czesc, jestes', name, 'i masz',age, 'lat')

print_age(name, age)


# ========================== ROZDZIAŁ 5 KONTENERY ( list, krotki, zbiory) ==============================
print("witaj".upper())

print('SIEMANKO MALE LITERY'.lower())

print('Witaj'.replace("j", "m"))

fruit = '[mango, banan, gruszki]'

print(fruit)


random = [] 
random.append(True)
random.append(100)
random.append(1.1)
random.append('Witaj')

print(random)

fruit = ['mango', 'banan', 'gruszki']
print(fruit[0])
print(fruit[1])

colors = ['niebieski', 'czerwony', 'zielony']
print(colors)

colors[2] = 'fioletowy'
print(colors)

colors2 = ['pomaranczowy', 'czarny', 'pistacjowy']
print(colors + colors2)
print('pomaranczowy' in colors2)
print('granatowy' not in colors2)

print(len(colors + colors2))

# Zagadka :) 

guess = input('Zgadnij jaki kolor wybralem: ')

if guess in (colors + colors2):
    print('Brawo! To wlasnie ten kolor! ;) ')
else:
    print('Niestety nie, ale sprobuj jescze raz :)')

my_tuple = ()
print(my_tuple)

dys = ('tata', 'mama', 'ja')
print(dys)
colors = ['niebieski', 'czerwony', 'zielony']
print(colors)

colors[2] = 'fioletowy'
print(colors)
colors = ('niebieski', 'czerwony', 'zielony')
print(colors[2])

print('zielony' in colors)
print('fioletowy' in colors)

print('bezowy' not in colors)
print('niebieski' not in colors) 

my_dict = dict({'agrest':'zielony',
                'porzeczka':'czerwona'})
print(my_dict)

my_dict2 = {'slonce':'plaza', 'woda':'ziemia'}
print(my_dict2)
print('=============================================')
facts = dict()

facts['programowanie'] = 'zabawa'
print(facts['programowanie'])
facts['komputer'] = 'elektornika'
facts['umysl'] = 'inteligencja'
facts['grunwald'] = '1410'
print(facts)

print('umysl' in facts)  # W sloniku mozna sprawdzac czy jest dany klucz, nie mozna sprawdzic czy jest dana wartosc. 
print('grunwald' in facts) 
print('1410' in facts) # tutaj sprawdzalem czy moge sprwadzic czy w danym slowniku jest wartosc - nie mozna sprwadzic.

# mozna usuwac takze pary ze slownika, uzywajac komendy del:

del facts['komputer']
print(facts)

# PISZEMY PROGRAM: 
print('=============================================')
print()

drinks = {'1':'whisky',
        '2':'wodka',
        '3':'gin & tonic',
        '4':'metaxa',
        '5':'brandy',
        '6':'rum & coke'}

chose = input('wybierz numer od 1 - 6: ')


if chose in drinks:
    alko = drinks[chose]
    print()
    print('dzisiaj otrzymujesz gratis alkohol: ', alko,'\n')
else:
    print('\n*** cos poszlo nie tak. Sprobuj jeszcze raz! ***\n')



# KONTENERY W KONTENERACH :

lists = []
rap = ['Eminem', 'Kanye West', 'Jay Z', 'Nas']

rock = ['Bob Dylan', 'The beatless', 'Led Zeppelin']

djs = ['Zeds Dead', 'Decks', 'Tiesto']

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

rap = lists[0]
print(rap)

rap = lists[0]
rap.append('Dr.Dre')
print(rap)
print(lists)

print('===================================================')

locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)  # to sa krotki, niezmienne obiekty , klucz - wartosc.
print()
eights = ['Edgar Allan Poe',
            'Charles Dickens']
        
nines = ['Hemingway', 
        'Fitzgerald',
        'Orwell']

authors = (eights, nines)
print(authors)
print()
bday = {'Hemingway':'7.21.1899',
        'Fitzgerald':'9.24.1896'}

my_list = bday
print(my_list)

my_tuple = (bday,)
print(my_tuple)


ny = {'lokalizacja': (40.7128, 74.0059),

    'celebryci': ['W.Allen','Jay Z', 'K.Bacon'],

    'fakty': {'stan': 'NY', 'kraj':'Ameryka'}}
print(ny)


# ZADANIA : strona 82.
# Zadanie 1:

muzycy = ['kanye', 'eminem', 'bruno mars']

print(muzycy)

# Zadanie 2:

miejsca = ('Warszawa : 23.224, 44.456',
            'Poznan: 66.234, 23.877')
print(miejsca)

#zadanie 3
print()
''' '''
slownik = dict()
slownik = {'187':'wzrost',
            'piwny':'kolor oczu',
            '83':'masa ciala',
            'Ryan Gosling':'ulubiony aktor',
            'czarny':'ulubiony kolor'}
        
print(slownik)
# print(slownik['kolor oczu'])

# Zadanie 4:


pytanie1 = input('Podaj moj wzrost ciala: ')
if pytanie1 in slownik:
    odp = slownik[pytanie1]
    print('dobra odpowiedz!')
else:
    print('chyba mnie nie znasz za dobrze !')

pytanie2 = input('Podaj moj kolor oczu: ')
if pytanie2 in slownik:
    odp = slownik[pytanie2]
    print('swietnie !')
else:
    print('No chyba jednak nie.')

pytanie3 = input('Podaj prosze moja mase ciala: ')
if pytanie3 in slownik:
    odp = slownik[pytanie3]
    print('bardzo dobrze ... !')
else:
    print('No niestety nie... ')

pytanie4 = input('Podaj moj ulubiony kolor: ')
if pytanie4 in slownik:
    odp = slownik[pytanie4]
    print('Super ! Dobra odpowiedz!')
else:
    print('Niestety nie... ! ')
'''

'''
autor = "kawka"
print(autor[3])
print(autor[-3])

print(range(1, 15, 2))

a = (' kot ' + 'w ' + 'butach') * 4
print(a)

# ____________________CAPITALIZE()  - po prostu zmienia pierwsza litere zdania na Wielka litere.

zdanie = 'to jest wynik naszej historii'
print(zdanie)

# ____________________FORMAT:

s = 'William {}'.format('Faulkner')
print(s)

print('Pioter {}'.format('Folkovecky'))

author = 'William' 
year_born = '1897'
print(''' #{} urodzil sie w {} roku.'''\
    #.format(author, year_born))


#n1 = input('wpisz rzeczownik: ')
#v = input('wpisz czasownik: ')
#p = input('wpisz przymiotnik: ')
#v2 = input('wpisz jeszcze raz rzeczownik: ')

# result = ''' Oto {} {} taka {} {} i scial wszystkie drzewaw okolicy.'''\
#    .format(n1, v, p, v2)

#print(result)


# d = '''Siemanko, oto przyklad dzialania funkcji SPLIT. Ta skladnia zostala podzielona na 2 zdania.'''.split('.')
# print(d)

# ________________________________________METODA JOIN:________________________________________
'''
words = ['zwinny', 'lis', 'przeskoczy', 'nad', 'leniwym', 'psem', '.']

new_syntax = ' '.join(words)

print(new_syntax)

# METODA ZAMIANY:

words2 = 'zwinny lis przeskoczy nad leniwym psem'

words2 = words2.replace('zwinny','sprytny')
print(words2)

ad = 'imperialny'
cd = ad.index('r')
print(cd)

try:
    'impretialny'.index('x')
except ValueError:
    print('nie znaleziono znaku.')

print('kot' in 'kot w butach')

print('Odpowiedziala mu: "Owszem".')


print('kot' in 'kot w butach')

words = ['zwinny','lis','przeskoczy','nad','leniwym','psem']

print(words[0:3])

# ZADANIE 1. / 93
print('"CAMUS"'.lower())

# Zadanie 2 / 93

ab = input('podaj rzeczownik: ')
ac = input('podaj osobe: ')

zdanie = ''' #Wczoraj napisalem {} i wyslalem do {}.'''\
    #.format(ab, ac)
'''
#print(zdanie)

# Zadanie 3 /93

z = ('aldous Huxley urodzil sie w 1894 roku.'.capitalize())
print(z)


# Zadanie 4:
print()
lancuch = '"Gdzie teraz? Kto teraz? Kiedy, teraz?"'
print(lancuch)

print(lancuch.split('?'))

# Zadanie 5:

fox = ['Zwinny', 'lis', 'przeskoczyl', 'nad', 'leniwym', 'psem', '.']
fox = ' '.join(fox)
fox = fox[0:-2] + '.'

print(fox)

# Zadanie 6

txt = 'W czasie suszy szosa sucha.'
txt = txt.replace('s', '$')
print(txt)

# Zadanie 7

w = 'Hemingway'.index('m')
print(w)

# Zadanie 8

w = 'to sa slowa ktore tworza lancuch znakow'
# Zadanie 9 

concat = '" trzy" + " trzy" + " trzy"'
mult = " trzy" * 3

print(concat)
print(mult)

# Zadanie 10

zdanie = 'Dlugo na szturm i szaniec pogladal w milczeniu. Na koniec rzekl: "Stracona."'

ind = zdanie[:48]

print(ind)
'''
# ====================================  ROZDZIAL 7 ==========================================


'''
# ________________________________________PĘTLE________________________________________
name = 'Ted'
for litery in name:
    print(litery)

tytuly = ['Jaka to melodia', 'Wyspa Tajemnic', 'Stary czlowiek i morze']

for example in tytuly:
    print(example)
print()

krotki = ('Programowanie', 'Znajomi', 'Chillout')

for names in krotki:
    print(names)
print()

people = {'Fowler':'Wzorce projektowe', 
'Knuth':'Algorytmy',
'Stroustrup':'C++'}

for characters in people:
    print(characters) 
                        # i tutaj np. petla zastosowala sie tylko do KLUCZY.


# wprowadzamy zmiany w modyfikowalnej danej iterowalnej:


tv = ['jaka to melodia', 'spadkobiercy', 'familiada', 'jeden z 10']

i = 0

for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
    
print(tv)

# LUB DRUGI SPOSOB NA TE SAMA PETLE :

tv = ['jaka to melodia', 'spadkobiercy', 'familiada', 'jeden z 10']

for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

print() 
# __________________________________ŁĄCZENIE NP. DWÓCH PETLI FOR:________________________________________

tv = ['jaka to melodia', 'spadkobiercy','familiada', 'jeden z 10']

coms = ['programowanie', 'znajomi', 'chillout']

all_shows = [] 

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show2 in coms:
    show2 = show2.upper()
    all_shows.append(show2)

print(all_shows)

# FUNKCJA RANGE: 

for i in range(0,11):
    print(i)
''' '''
# PĘTLA WHILE:

x = 9
while x > 0:
    print('{}'.format(x))
    x -= 1
print('0! \nwoohoo')

while True:
    print('hello!')


# ________________________________________INSTRUKCJA BREAK:________________________________________

for i in range(0,21):
    print(i)
pass

for i in range(11,21):
    print(i)
    break

for i in range(11,21):
    print(i)
    if i == 18:
        break

print( 3 % 3 )
qs = ['jak masz na imie: ',
    'jaki jest Twoj ulubiony kolor: ',
    'jakie masz zadanie: ',
    'jak mamy dzis dzien: ']

i = 0

while True:
    print('*** Wpisz q, aby zakonczyc. ***')
    a = input(qs[i])
    if a == 'q':
        print('************** PRZERWANO **************')
        break
    i = (i + 1) % 4

# ____________________________________INSTRUKCJA CONTINUE_________________________________________


for i in range(0,15):
    if i == 9:
        continue
    if i == 11:
        continue
    print(i)

# ____________________________________ PETLE ZAGNIEZDZONE _______________________________________


for i in range(1, 4):
    print(i)
    for letter in ['a', 'b', 'c']:
        print(letter)
print('========================================')
pass

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = [] 
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

# ZAGNIEZDZANIE PETLI FOR W PETLI WHILE: 

while input('tak lub nie: ') != 'nie':
    for i in range(1,6):
            print(i)


# ZADANIE 1 / 104
# wyswietl wszystkie elementy listy:


lista = ['Noc zywych trupow', 'ekipa', 'rodzina soprano', 'pamietniki wampirow']

for l in lista:
    print(l)


# ZADANIE 2:
# wyswietl wszystkie liczby z zakresu od 25 do 50.

for n in range(25, 51):
    print(n)

# ZADANIE 3:
# Wyswietl wszystkie elementy z listy z zadania 1 wraz z ich indeksami.



lista = ['Noc zywych trupow', 'ekipa', 'rodzina soprano', 'pamietniki wampirow']

for i, show in enumerate(lista):
    print(i)
    print(show)

print()


# ZADANIE 4: 
# Napisz program zawierajacy petle nieskonczona (z opcja nacisniecia klawisza q w celu jej przerwania),
# oraz liste liczb. Podczas kazdej iteracji tej petli popros uzytkownika o odganiecie liczby z listy,
# a nastepnie wyswietlaj informacje, czy udalo mu sie poprawnie trafic , czy nie.

lucky_number = [11]

while True:
    answer = input('Odgadnij liczbe [0-20], lub wcisnij "q" aby przerwac gre: ')
    if answer == 'q':
        break

    try:
        answer = int(answer)
    except ValueError:
        print('\n**zle wpisana wartosc, miala byc liczba!\n**')
    if answer in lucky_number:
        print('\n**brawo, udalo Ci sie!\n**')
    else:
        print('\n** niestety.. to nie jest ta liczba! sprobuj jeszcze raz :) **\n')

# ZADANIE 5: 
# Pomnoz wszystkie liczby z listy [8, 19, 148, 4] przez wszystkie liczby z listy [9, 1, 33, 83], a uzykane wyniki zapisz
# w trzeciej liscie.

numb1 = [8, 19, 148, 4]
numb2 = [9, 1, 33, 83]

numbs = [] 

for show1 in numb1:
    for show2 in numb2:
        mult = show1 * show2
        numbs.append(mult)
        print(mult)


# ================================================= ROZDZIAŁ 8 MODUŁY =======================================================


print(2**3)

import math

print(math.pow(2, 3))

import random

print(random.randint(0, 100))

import statistics

numbers = [1, 5, 33, 12, 46, 33, 2]

# obliczy srednia: 

print(statistics.mean(numbers))

# Obliczy medianę:

print(statistics.median(numbers))

# Obliczy dominante:

print(statistics.mode(numbers))

# FUNKCJA SPRAWDZAJACA CZY DANE SLOWO JEST 'SLOWEM KLUCZ' DLA PROGRAMU PYTHON: "keyword"

import keyword

print(keyword.iskeyword('for'))
print(keyword.iskeyword('in'))
print(keyword.iskeyword('i'))
print(keyword.iskeyword('while'))

# Zadanie 1 / 108
# Wywolaj kilka innych funkcji z modulu statistic.
print('=============================================')
import statistics

print(statistics.multimode(numbers))
print(statistics.quantiles(numbers))
print(statistics.median_high(numbers))

# Zadanie 2 / 108
# Utworz modul o nazwie 'cubed' definiujacy funkcje pobierajaca jako parametr liczbe i zwracajaca te liczbe podniesiona do potegi trzeciej.
# Zaimportuj ten modul w innym. 

from tstp import cubed

print(cubed.funkcja(6))

import math

print(math.pow(3,3))
'''
'''
# ================================ ROZDZIAL 12 PARADYGMATY PROGRAMOWANIA ================================================== #
# Cwiczenia:


class Orange:
    def __init__(self):
        self.self
    print("Utworzono!")
#
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
    print("Utworzono!!")

or1 = Orange(280, 'ciemnopomaranczowy')
print(or1)

#
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
    print("Utworzono!!")

or1 = Orange(280, 'ciemnopomaranczowy')
print(or1.weight)
print(or1.color)

#
print()

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
    print("Utworzono!!")

or1 = Orange(280, 'ciemnopomaranczowy')
or1.weight = 650
or1.color = 'jasnopomaranczowy'

print(or1.weight)
print(or1.color)
#
'''

#___________________________________________________________ UDEMY PROGRAMOWANIE OBIEKTOWE:___________________________________________


# OBIEKTY - to pojemniki do przechowywania zmiennych i fuknkcji tematycznie ze soba powiazanych 
#            do dalszego latwiejszego ponownego wykorzystania. 

# Klasy - foremki ( szablony ) do tworzenia egzemplarzy obiektów.

# Atrybut - cecha opisujaca obiekt.

# Metoda - funkcja, która operuje na obiekcie. 

# Self - z ang. 'JA', 'sam osobiscie' , 'siebie' w innych jezykach 'this'. Pobiera wywolywana obiektów do funkcji.

# _____ init _____ - initialization - inicjalizacja - czyli ustawienie startowych wartosci dla atrybutów.
#                      ( w innych jezykach ___init___ to konstruktor ).









                                                                            # 1
                                                           
'''
age = 100

class Users:
    age = 0



    def print_age(self, message):
        print(message, 'wiek: ', self.age)
    
    def another_method(self, wiadomosc):
        print(wiadomosc, 'Twoj wiek to ', self.age)

    def another_next(self, message, blablabla):
        pass


seba = Users()
mirek = Users()
arek = Users()

mirek.age = 24
arek.age = 50

mirek.print_age('plec: mezczyzna:')
arek.print_age('plec: mezczyzna,')


def print_age(name, age):
    print(name, 'wiek: ', age)

name = "Arek"
print_age(name, age)

'''


                                                                         # 2
'''

age = 150

class Users:
    age = 0
    name = ""


    def print_age(self, message):
        print(message, 'wiek:', self.age, 'imie:', self.name)
    

    def another_next(self, message, blablabla):
        pass


user1 = Users()
user2 = Users()


user1.age = 24
user1.name = "Arkadiusz"
user1.print_age('plec: mezczyzna,')


user2.age = 50
user2.name = "Mirek"
user2.print_age('plec: mezczyzna,')


def print_age(name, age):
    print(name, 'wiek:', age)

name = "Dziadek,"
print_age(name, age)
'''
                                                                       # 3
'''

age = 150

class Users:         # klasy warto pisac z wielkiej litery.
    age = 0
    name = ""


    def print_age(self, message):
        print(message, self.name, 'wiek:', self.age)
    

    def another_next(self, message, blablabla):
        pass


userList = [Users(), Users()]

userList[0].name = "Remigiusz,"
userList[0].age = '30'
userList[0].print_age('To jest')

userList[1].name = 'Franek,'
userList[1].age = '50'
userList[1].print_age('A to jest')



def print_age(name, age):
    print(name, 'wiek:', age)

name = "Dziadek,"
print_age(name, age)

'''
'''

# ___________________________________________________________________ init ____________________________________________________
age = 150

class Users:


    def __init__(self, age, name):
        print('self - inicjator, ktory wywoluje sie zawsze podczas konstrukcji obiektu.')


        self.age = age
        self.name = name

        self.ageInFuture = age + 1

    def print_informations(self, message):
        print(message, 'wiek:', self.age, 'imie:', self.name)
    

    def another_next(self, message, blablabla):
        pass


user1 = Users(24, 'Arek')
user2 = Users(50, 'Mirek')


user1.print_informations('plec: mezczyzna,')
user2.print_informations('plec: mezczyzna,')


def print_informations(name, age):
    print(name, 'wiek:', age)

name = "Dziadek,"
print_informations(name, age)

print('Arek w przyszlym roku bedzie mial lat:', user1.ageInFuture)

'''


# ____________________________________________ powtorka informacji z petli. _______________________________________

#import json
'''
import math
print(math.sqrt(9))
from math import *

print(sqrt (64))


print(4**12)

'''
'''

a = int(input('podaj liczbe: '))
b = int(input('podaj druga liczbe: '))

print(a + b)

''''''

imie = input('Podaj swoje imie: ')
wiek = input('podaj swoj wiek: ')

age_in_future = (int(wiek) + 1)

print('Hej', imie, 'masz', wiek, 'lat, a w przyszlym roku bedziesz mial ', age_in_future, 'lat')
'''


'''
suma = 0

i = 0

while i < 4:
    x = int(input('Podaj dowolna liczbe: '))
    suma += x
    i += 1

print('Suma liczb wynosi', suma)
'''
'''
wynik = 0

for i in range(5):
    x = int(input('podaj liczbe: '))
    wynik += x
    if (i % 2 == 1):
        print('nieparzysta')
    else:
        print('liczba parzysta')

print('Wynik dodawania liczb to: ', wynik)

'''
'''
for i in range(0,201):
    if (i % 5 == 0 and i % 7 != 0):
        print('liczba', i, 'jest podzielna przez 5 oraz niepodzielna przez 7')
    else:
        pass




print(50%12)

'''

wynik = 0

i = 0

while i < 3:
    x = int(input('prosze podac liczbe parzysta i dodatnia: '))
    if (x > 0 and x % 2 == 0 and x > 0):
        wynik += x
    else:
        print('miala byc liczba parzysta i dodatnia! sprobuj ponownie.')
        continue
    print('aktualny wynik dodawania to:', wynik)
    i += 1

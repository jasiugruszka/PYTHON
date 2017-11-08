imie = input('Wprowadz imie:')
print ('Witaj, ' + imie + '!')
tekst = '''
    Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
    Ile cię trzeba cenić, ten tylko się dowie,
    Kto cię stracił. Dziś piękność twą w całej ozdobie
    Widzę i opisuję, bo tęsknię po tobie.

    Panno Święta, co Jasnej bronisz Częstochowy
    I w Ostrej świecisz Bramie! Ty, co gród zamkowy
    Nowogródzki ochraniasz z jego wiernym ludem!
    Jak mnie dziecko do zdrowia powróciłaś cudem
    (Gdy od płaczącej matki pod Twoję opiekę
    Ofiarowany, martwą podniosłem powiekę
    I zaraz mogłem pieszo do Twych świątyń progu
    Iść za wrócone życie podziękować Bogu),
    Tak nas powrócisz cudem na Ojczyzny łono.
    Tymczasem przenoś moję duszę utęsknioną
    Do tych pagórków leśnych, do tych łąk zielonych,
    Szeroko nad błękitnym Niemnem rozciągnionych;
    Do tych pól malowanych zbożem rozmaitem,
    Wyzłacanych pszenicą, posrebrzanych żytem;
    Gdzie bursztynowy świerzop, gryka jak śnieg biała,
    Gdzie panieńskim rumieńcem dzięcielina pała,
    A wszystko przepasane, jakby wstęgą, miedzą
    Zieloną, na niej z rzadka ciche grusze siedzą. '''
l = tekst.lower()
s = tekst.count(' ')
p = tekst.count(',')
k = tekst.count('.')
z = len(tekst)
g = (l.count('a')+ l.count('e')+ l.count('i')+ l.count('o')+ l.count('u')+ l.count('y') + l.count('ą') + l.count('ó'))   
print ('Tekst składa się z ',z,'znaków, w tym: ',g,'samogłosek, ',k,'kropek, ',p,'przecinków i ',s,'spacji.')


print('Co drugi, co trzeci i co siódmy znak:')
print(tekst[::2], tekst[::3], tekst[::7])


lista = tekst.splitlines()
print ('\n' + lista[1])

print (tekst.upper())

print (tekst.replace('Litwo!', 'Polsko!'))




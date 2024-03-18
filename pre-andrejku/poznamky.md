# Rezy
### syntax - `[START:STOP:KROK]`

START je index na ktorom zacne(aj vypise)

STOP je index na ktorom zastane(pred nim to sekne tym padom tento index nebude vypisany),


KROK je po kolkatich pismenkach ide(zakladna hodnota je 1, vypise pismenko po pismenku)

### priklad

`print("Andrej"[0:2])` vypise -> `An`

Pretoze: An|drej , pred druhym indexom nastane rez.

## Indexy

Kazde pismenko v retazci ma index(poziciu).

Napriklad: V retazci `"Andrej"` budu hodnoty -> A=0 n=1 d=2 r=3 e=4 j=5 

Prakticky pocitame pismenka od nuly a to je ich index.

Taktiez to funguje z opacnej strany, len pocitame od -1 a nie od nuly.

Napriklad: V retazci `"Andrej"` budu hodnoty -> A=-6 n=-5 d=-4 r=-3 e=-2 j=-1 


## Podstatna cast(bolo na pisomke)

`r = "rozok"`

`print(r[0:2]+r[3:5])`

Vypise `rook`, `z` je preskocene pretoze koncime na 2 indexe(rez je pred nim vykonany) a pokracujeme na tretom indexe. Cize druhy index (`z`) sa nikdy nevypise.
Python to vidi takto -> `ro|z|ok`


`print("andrejka"[-3:-6:-1])`

Vypise `jer`, pretoze zacne na `r` skonci na `j` a potom to Krok cele prehodi kedze -1 ide od zadu. Dostaneme tym padom `jer`


### Funkcia len()

jej sytax zapisu je `len("retazec alebo veta to je jedno")` alebo `len(premenna)` <- `premenna` musi byt ale definovana!
Dostaneme dlzku retazca.

### Funkcia range()

Dostaneme list cisel. Pri jej volani MUSI dostat cislo, nie retazec!
- ZLE: `range("123")` alebo `range(string)` (ratam s tym ze premenna `string` drzi retazec)
- DOBRE:  `range(123)` alebo `range(len(string))` <- dostane dlzku retazca z premennej a dosadi ju

Priklad pouzitia

`string = "ABCD"`

`for i in range(len(string)):`

`    print(string[i])`

vypise postupne pod seba pismenka(vybera ich podla indexu od 0 az po koniec retazca)

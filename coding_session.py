"""Pohlédněte na následující reprezentaci receptu:
Uložte si tuto strukturu do proměnné recept na začátek nového programu. Vypište pomocí funkce print kolik bude celé jídlo stát korun
zaokrouhlené na celé koruny nahoru.


recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}
celkem = 0
for radek in recept['ingredience']:
    #cislo = radek[2].split()[0]
    #cislo = radek[2].replace(" kč", "")
    #cislo = radek[2].strip(" kč")
    cislo = radek[2][:-3]
    celkem += float(cislo)
    print(celkem)

print (round(celkem)) """



"""Čtení na doma - funkce filter
K výběru určitých hodnot ze slovníku můžeme použít i funkci filter(). 
Tato funkce je zpravidla používána s tzv. anonymní funkcí, tj. funkcí, která nemá žádné jméno. Je to z důvodu, že funkce je 
použita pouze na tomto místě a nepotřebujete tedy jméno, aby byla volána. Anonymním funkcím se často říká i lambda funkce, 
protože se k jejich definici používá klíčové slovo lambda.

Níže je příklad, jak použít funkci filter() k výběru knih, které vyšly v roce 2019.
"""
books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

seznam_knih = []
# for radek in books:
#     if radek["year"] == 2019:
#         seznam_knih.append(radek)
# print(seznam_knih)

# způsob pomocí vlastní fce
def is_2019(book):
    return book["year"] == 2019 # výsledek fce je buď pravda nebo nepravda

# potom můžu tu funkci takhle volat
# for radek in books:
#     if is_2019(radek):
#         seznam_knih.append(radek)
# print(seznam_knih)

books = list(filter( lambda book: book["year"] == 2019, books))
print(books)

# vylepšení
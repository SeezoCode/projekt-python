'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

slovnik_aut = {
    'skoda': {
        'model': 'Octavia',
        'condition': 1.,
        'working': True,
        'doors': ('front left', 'front right', 'back left', 'back right', 'trunk'),
        'wheel_condition': [80, 76, 81, 84],
        'voice_commands': {'play music', 'navigate', 'autopilot', 'call'}
    },
    'tesla': {
        'model': 'model 3',
        'condition': .23,
        'working': False,
        'doors': ('front left', 'back right', 'trunk', 'frunk'),
        'wheel_condition': [25, 19, 32, 14],
        'voice_commands': {'navigate', 'autopilot', 'crash', 'mine bitcoin'}
    },
    'volkswagen': {
        'model': 'golf',
        'condition': .90,
        'working': True,
        'doors': ('front left', 'front right', 'back left', 'back right', 'trunk'),
        'wheel_condition': [67, 80, 56, 66],
        'voice_commands': {'play music', 'navigate', 'call'}
    }
}


def print_slovnik(slovnik: dict):
    lengths = (16, 9, 7, 70, 24, 65)
    print("brand", " " * 4, ': ', end='')
    [print(x + " " * (lengths[i] - len(x)), end=' |') for i, x in enumerate(list(slovnik[list(slovnik.keys())[0]]))]
    print()
    for car_name in slovnik:
        print(car_name + " " * (11 - len(car_name)), end=': ')
        [print(f'{" " * (lengths[i] - len(str(slovnik[car_name][x])))}{slovnik[car_name][x]}', end=' |') for i, x in
         enumerate(list(slovnik[car_name]))]
        print('')


print_slovnik(slovnik_aut)

slovnik_aut.pop('tesla')

print('\n\n')

slovnik_aut['CarsMovie'] = {
    'model': 'Blesk McQueen',
    'condition': 1.,
    'working': True,
    'doors': ('front left', 'front right', 'back left', 'back right', 'trunk'),
    'wheel_condition': [100, 100, 100, 100],
    'voice_commands': {'play music', 'navigate', 'go really fast', 'win all races'}
}

print_slovnik(slovnik_aut)

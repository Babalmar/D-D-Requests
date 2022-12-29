import requests
import random

def monster():
    response2 = requests.get('http://www.dnd5eapi.co/api/monsters')
    a2 = response2.json()

    lista2 = a2['results']

    c = len(lista2) - 1
    monsters = []
    for item in lista2:
        monsters.append(lista2[c]['index'])
        c -= 1

    random_monster = random.choice(monsters)
    response3 = requests.get('http://www.dnd5eapi.co/api/monsters/'+ random_monster)
    d = response3.json()
    print('Name: {}, Type: {}, Hit points: {}, Hit dice: {}, Armor class: {}'.format(d['name'], d['type'], d['hit_points'], d['hit_dice'], d['armor_class']))




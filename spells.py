import requests
import random

def spell():
    response = requests.get('http://www.dnd5eapi.co/api/spells')
    spells_response = response.json()

    lista = spells_response['results']

    spells_id = len(lista) - 1
    spells = []
    for item in lista:
        spells.append(lista[spells_id]['index'])
        spells_id -= 1

    random_spell = random.choice(spells)
    response1 = requests.get('http://www.dnd5eapi.co/api/spells/'+ random_spell)
    a1 = response1.json()

    print('Name: {}\nDescription: {}'.format(a1['name'], ' '.join(a1['desc'])))
    if 'higher_level' in a1:
        print('Higher level: {}'.format(' '.join(a1['higher_level'])))
    print('Range: {}\nComponents: {}'.format(a1['range'], ' '.join(a1['components'])))
    if 'material' in a1:
        print('Materials: {}'.format(a1['material']))
    print('Casting time: {}\nLevel: {}\nSchool: {}'.format(a1['casting_time'], a1['level'], a1['school']['name']))

    lista = a1['classes']

    classes_id = len(lista) - 1
    classes = []
    for item in lista:
        classes.append(lista[classes_id]['name'])
        classes_id -= 1
    
    print('Classes:')
    for profession in sorted(classes):
        print(profession)

spell()
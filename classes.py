import requests
import random

def hero_class():
    response = requests.get('http://www.dnd5eapi.co/api/classes')
    classes_response = response.json()

    lista = classes_response['results']

    class_id = len(lista) - 1
    classes = []
    for item in lista:
        classes.append(lista[class_id]['index'])
        class_id -= 1

    random_class = random.choice(classes)
    response1 = requests.get('http://www.dnd5eapi.co/api/classes/'+ random_class)
    a1 = response1.json()
    print('Name: {}, Hit die: {}'.format(a1['name'], a1['hit_die']))

hero_class()

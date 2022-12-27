import requests
import random

def equipment():
    response = requests.get('http://www.dnd5eapi.co/api/equipment')
    equipment_response = response.json()

    lista = equipment_response['results']

    equipment_id = len(lista) - 1
    equipment = []
    for item in lista:
        equipment.append(lista[equipment_id]['index'])
        equipment_id -= 1

    random_equipment = random.choice(equipment)
    response1 = requests.get('http://www.dnd5eapi.co/api/equipment/'+ random_equipment)
    a1 = response1.json()
    print('Name: {}, Category: {}, Cost: {} {}'.format(a1['name'], a1['equipment_category'], str(a1['cost']['quantity']), a1['cost']['unit']))
    if a1['equipment_category'] == 'Weapon':
        print('Weapon category: {}, Weapon range: {}, Damage dice: {}, Damage bonus: {}, Damage type: {}'.format(a1['weapon_category'], a1['weapon_range'], a1['damage']['damage_dice'], str(a1['damage']['damage_bonus']), a1['damage']['damage_type']['name']))
    
equipment()
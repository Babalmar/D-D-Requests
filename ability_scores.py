import requests
import random

def abilities():
    response = requests.get('http://www.dnd5eapi.co/api/ability-scores')
    equipment_response = response.json()

    lista = equipment_response['results']

    equipment_id = len(lista) - 1
    equipment = []
    for item in lista:
        equipment.append(lista[equipment_id]['index'])
        equipment_id -= 1

    random_ability_score = random.choice(equipment)
    response1 = requests.get('http://www.dnd5eapi.co/api/ability-scores/'+ random_ability_score)
    a1 = response1.json()

    lista = a1['skills']

    skill_id = len(lista) - 1
    skills = []
    for item in lista:
        skills.append(lista[skill_id]['name'])
        skill_id -= 1
    
    print('Name: {}\nDescription: {}\nSkills:'.format(a1['full_name'], ' '.join(a1['desc'])))
    for skill in sorted(skills):
        print(skill)



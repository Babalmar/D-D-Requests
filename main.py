import ability_scores as stats
import classes
import equipment as eq
import spells
import monsters

def dd_requests():
    text = '''Choose what information you want to fetch?\n
    1 - Ability scores\n
    2 - Classes\n
    3 - Equipment\n
    4 - Spells\n
    5 - Monsters\n'''
    
    while True:
        option = input(text)   
        if option not in (1, 2, 3, 4, 5):
            print("Not an appropriate choice.")
        else:
            break
    if int(option) == 1:
        stats.abilities()
    elif int(option) == 2:
        classes.hero_class()
    elif int(option) == 3:
        eq.equipment()
    elif int(option) == 4:
        spells.spell()
    elif int(option) == 5:
        monsters.monster()
        
    
    
dd_requests()
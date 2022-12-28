import ability_scores
import classes
import equipment
import spells
import monsters

def dd_requests():
    text = '''Choose what information you want to fetch?\n
    1 - Ability scores\n
    2 - Classes\n
    3 - Equipment\n
    4 - Spells\n
    5 - Monsters\n'''
    
    option = input(text)
    
    if int(option) == 1:
        monsters.monster()
        
    
    
dd_requests()
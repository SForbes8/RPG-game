'''
RPG game

CREDITS

Programming: Sam Forbes
Story: Charlie Whiteley
Story Components: Mark Molnar
'''

#Classes
class npc:
    def damage(self,amount):
        self.hp -= amount
class goblin(npc):
    def __init__(self):
        self.type = 'goblin'
        self.hp = 50
        self.hit_chance = 80
        self.crit_chance = 10
        self.dmg = 10

class orc(npc):
    def __init__(self):
        self.type = 'orc'
        self.hp = 100
        self.hit_chance = 85
        self.crit_chance = 15
        self.dmg = 15

class Player:
    def __init__(self):
        self.hp = 100
        self.hit_chance = 90
        self.crit_chance = 10
        self.max_hp = 100
        self.gold = 0
        self.potions = 1
        self.potionm = 0
        self.potionl = 0
    def damage(self,amount):
        self.hp -= amount

class shop:
    def __init__(self,list):
        self.items = list[0:][0]
        self.prices = list[0:][1]
        self.stock = list[0:][2]
    def run(self):
        print('You have {player.gold} gold.\n')
        print('Welcome to the shop! Here you can buy:')
        while choice != len(self.items)+1:
            for i in range(len(self.items)):
                self.txt = [self.items[i]+': '+self.prices[i]+' gold ('+self.stock[i]+' in stock.)']
            choice = decision(self.txt+['Nothing'],message='What do you want to buy?')
            if choice != len(self.items)+1: #If the choice isn't 'Nothing'
                if self.prices[choice-1] <= player.gold:
                    print(f'Thank you for buying the {self.items[choice-1]}!')
                    self.stock[choice-1] -= 1
                    player.gold -= self.prices[choice-1]
                    print('You have {player.gold} gold remaining.\n')
                    if self.stock[choice-1] <= 0:
                        del self.stock[choice-1],self.items[choice-1],self.prices[choice-1]
                else:
                    print('You don\'t have enough gold!\n')
        print('Thanks for visiting!')
#Functions
def decision(options,message='What do you choose to do?'):
    for i in range(len(options)):
        print(f'{i+1}){options[i]}')
    if len(options) == 2:
        return int(input(f'{message} (1/2): '))
    else:
        return int(input(f'{message} (1-{str(len(options))})'))

def percent_chance(chance):
    x = randint(1,100)
    if chance >= x:
        return True
    return False

def battle(enemy):
    if type(enemy) == list:
        pass #Many enemies
    else:
        print(f'You have entered a battle with one {enemy.type}!')
        while player.hp > 0 and enemy.hp > 0:
            print(f'You have {player.hp} hp.')
            print(f'The {enemy.type} has {enemy.hp} hp.\n')
            success = False
            choice = decision([f'Attack with your {sword_type}',f'Use {health_potion_type} ({player.potions} remaining)','Dodge before attacking'])
            if sword_type == 'rusty sword':
                damage = 12
            elif sword_type == 'iron sword':
                damage = 18
            elif sword_type == 'steel sword':
                damage = 27
            if health_potion_type == 'small health potion (restores 50hp)':
                restore = 50
            if choice == 1:
                if percent_chance(player.hit_chance):
                    enemy.damage(damage)
                    print(f'You dealt {damage} damage with your {sword_type}!')
                else:
                    print('Oops! You missed...')
            elif choice == 2:
                if player.potions > 0:
                    oldhp = player.hp
                    player.hp += restore
                    if player.hp > player.max_hp:
                        player.hp = player.max_hp
                    player.potions -= 1
                    print(f'You restored {player.hp-oldhp} hp. You have {player.potions} left.')
                else:
                    print('You had no potions!')
            elif choice == 3:
                success = percent_chance(40)
                if success:
                    enemy.damage(damage)
                    print(f'You dodged successfully and then dealt {damage} damage!')
                else:
                    print('Your dodge failed...')
            input('\n')
            if not success and enemy.hp > 0:
                if percent_chance(enemy.hit_chance) or choice == 34:
                    player.damage(enemy.dmg)
                    print(f'\nThe {enemy.type} hit you and dealt {enemy.dmg} damage!')
                else:
                    print(f'\nThe {enemy.type} missed!')
            print('\n')
        if player.hp <= 0:
            print('Game Over...')
            exit()
        print(f'You beat the {enemy.type}!')
        gold_chance = randint(1,100)
        if enemy.type == 'goblin':
            if gold_chance <= 30: #30% chance of no drops
                print('The goblin dropped nothing...')
            elif gold_chance <= 80: #50% chance of 15 gold
                print('The goblin dropped 15 gold!')
                player.gold += 15
                print(f'\nYou now have {player.gold} gold!')
            else: #20% chance of 30 gold
                print('The goblin dropped 30 gold!')
                player.gold += 30
                print(f'\nYou now have {player.gold} gold!')
        elif enemy.type == 'orc':
            if gold_chance <= 30: #30% chance of 15 gold
                print('The orc dropped 15 gold!')
                player.gold += 15
                print(f'\nYou now have {player.gold} gold!')
            elif gold_chance <= 80: #50% chance of 30 gold
                print('The orc dropped 30 gold!')
                player.gold += 30
                print(f'\nYou now have {player.gold} gold!')
            else: #20% chance of 60 gold
                print('The orc dropped 60 gold!')
                player.gold += 60
                print(f'\nYou now have {player.gold} gold!')
#Imports/Dependencies
from time import sleep
from random import randint

#Init
player = Player()
sword_type = 'rusty sword'
health_potion_type = 'small health potion (restores 50hp)'

print('You are Corde Madine, a noble warrior of the country of Leden.\n')
print('You are being given an award for your work fighting for your country.')
input()
print('Suddenly, Walya and her army of goblins attack the city!')
choice = decision(['Stay and fight','Tell everyone to flee'])
if choice == 1:
    #Stay and fight
    '''
    You fight against a series of goblins, and it is very likely that the player will lose here. If they don't, they continue with a large amount of gold.
    You escape after 5 battles (option 1) or fight 100 more (option 2). Option 1: You escape to the shelter in Danr.
    '''
    pass
else:
    #Tell everyone to flee
    print('\nYou see that there are too many of them for the small amount of soldiers you have on hand.')
    print('Everyone runs for their lives as you and what\'s left of the other soldiers defend them.')
    input()
    goblin1 = goblin()
    battle(goblin1)
    del goblin1
    input()
    print('\nIt was a struggle but the citizens got out alive. They\'ve made a makeshift shelter in the mountains of Danr.')
    print('However, these conditions are not suitable for too long. You\'re going to take back the city!')
    input()
print('Before you re-infiltrate the city, many of the locals have come to wish you and your soldiers luck.')
print('The blacksmith comes up to you and offers:')
choice = decision(['His best armour or','His best sword.'],message='Which option to you choose?')
if choice == 1:
    print('You accepted the Iron Armour! Your max hp is now 150!')
    player.max_hp += 50
else:
    print('You accepted the Iron Sword! Your sword now deals 18 damage!')
    sword_type = 'iron sword'
input()
player.hp = player.max_hp
print(f'The local potion maker offers to refill your health! Your hp is now {player.max_hp}!')
input()
print('\nYou set off towards the city, but plan to stop off at the nearby village of Laton to pick up some supplies.')
print('You are following the path towards Laton when you come across a large patrol of goblins!')
choice = decision(['Sneak past','Fight them head on','Launch a surprise attack'])
if choice == 1:
    #Sneak past
    print('You sneak past and they don\'t notice you!')
elif choice == 2:
    print('They see you and attack one by one!')
    goblin1 = goblin()
    goblin2 = goblin()
    goblin3 = goblin()
    battle(goblin1)
    input()
    battle(goblin2)
    input()
    battle(goblin3)
    print('You defeated the patrol!')
    print('The last one dropped something: a piece of paper. It reads: follow the path west for supplies. - Consus the Orc')
    del goblin1,goblin2,goblin3
    input()
    print('You identify the path: it is slightly hidden on the west side. Do you:')
    choice = decision(['Follow the main path to Laton and ignore the note','Follow the hidden path west'])
    if choice == 2:
        print('You follow the path westwards. Suddenly you see a clearing!')
        orc1 = orc()
        print('In the clearing you see an orc protecting two potions. It sees you and immediately battles!')
        battle(orc1)
        input()
        print('You pick up the two small health potions, and return to where the patrol was.')
        player.potions += 2
        input()
else:
    print('You surprise them and two flee but one stays to fight!')
    goblin1 = goblin()
    battle(goblin1)
    input()
print('You continue on to Laton village for supplies.')
#Arrival at Laton Village
sleep(4)
print('You arrive at Laton Village.')
choice = 0
while choice != 3:
    print('There is an Orc guarding the exit to the village. You can:')
    laton_shop = shop([['small health potion (restores 50hp)',20,2],['medium health potion (restores 100hp)',30,1],[f'Iron {not_yet_got}',50,1]])
    choice = decision(['Look around','Visit the shop','Fight the orc to leave'])
    if choice == 1:
        #Sidequests
        pass
    elif choice == 2:
        laton_shop.run()

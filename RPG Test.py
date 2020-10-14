import random

class Player:
    def __init__(self,health,mp,defending):
        self.health = health
        self.mp = mp
        self.defending = False
    def status(self):
        print 'HP:',self.health
        print 'MP:',self.mp
    def attack(self):
        print 'You attack!'
        damage = random.randint(20,25)
        print 'You dealt',damage,'damage!'
        enemy.health -= damage
        print 'Enemy health:',enemy.health
    def defend(self):
        print 'You brace yourself!'
        self.defending = True
    def heal(self):
        print 'You heal yourself!'
        healing = random.randint(15,20)
        player.health += healing
        player.mp -= 10
        print 'You healed',healing,'HP, leaving you with',player.health,'health and',player.mp,'MP left!'
    def power_attack(self):
        print 'You imbue your sword with magic and lunge at the enemy!'
        damage = random.randint(30,40)
        print 'You dealt',damage,'damage, and spent 15 MP!'
        enemy.health -= damage
        print 'Enemy health:',enemy.health
        player.mp -= 15
class Enemy:
    def __init__(self,health,mp):
        self.health = 100
        self.mp = 100
    def attack(self):
        print 'You have been attacked!'
        if player.defending == False:
            damage = random.randint(20,25)
        else:
            damage = random.randint(10,13)
        print 'You have been dealt',damage,'damage!'
        player.health -= damage
        print 'Current health:',player.health
    def power_attack(self):
        print 'The enemy lunges at you with their claws, dealing massive damage!'
        if player.defending == False:
            damage = random.randint(30,40)
        else:
            damage = random.randint(15,20)
        print 'You take',damage,'damage!'
        player.health -= damage
        print 'Current health:',player.health
    def heal(self):
        print 'The enemy heals itself!'
        healing = random.randint(5,10)
        enemy.health += healing
        enemy.mp -= 15
        print 'The enemy healed',healing,',leaving it with',enemy.health,'health left!'
player = Player(100,100,False)
enemy = Enemy(100,100)
while player.health >= 0 and enemy.health >= 0:

    if player.health <=0:
        break

    option = raw_input("What would you like to do? (Type help for command list) ")
    if option == 'status':
        player.status()
    elif option == 'defend':
        player.defend()
    elif option == 'attack':
        player.attack()
    elif option == 'heal':
        player.heal()
    elif option == 'power attack':
        player.power_attack()
    elif option == 'help':
        print 'status: Check on your current stats'
        print 'attack: Deal damage to the enemy'
        print 'defend: Use your turn to take half damage from the enemy, if it attacks'
        print 'heal: use 10 MP to heal yourself 15-20 HP'
        print 'power attack: use 15 MP to deal 30-40 damage to the enemy'
        continue
    else:
        print 'Invalid option.'
        continue
    if enemy.health <=0:
        break
    enemy_choice = random.randint(1,3)
    if enemy_choice == 1:
        enemy.attack()
    if enemy_choice == 2:
        enemy.power_attack()
    if enemy_choice == 3:
        enemy.heal()
    player.defending = False
if player.health <= 0:
    print 'You have lost!'
if enemy.health <= 0:
    print 'You won!'
raw_input('Press enter to close.')

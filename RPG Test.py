import random

class Player:
    def __init__(self, health, mp, defending, evading):
        self.health = health
        self.mp = mp
        self.defending = False
        self.evading = False
    def status(self):
        print 'HP:',self.health
        print 'MP:',self.mp
    def attack(self):
        print 'You attack!'
        if enemy.defending == False:
            damage = random.randint(10,15)
        else:
            damage = random.randint(5,8)
        print 'You dealt',damage,'damage!'
        enemy.health -= damage
    def defend(self):
        print 'You brace yourself!'
        self.defending = True
    def heal(self):
        print 'You heal yourself!'
        healing = random.randint(15,20)
        player.health += healing
        if player.health > 100:
            player.health = 100
        player.mp -= 10
        print 'You healed',healing,'HP, leaving you with',player.health,'health and',player.mp,'MP left!'
    def power_attack(self):
        print 'You imbue your sword with magic and lunge at the enemy!'
        if enemy.defending == False:
            damage = random.randint(20,30)
        else:
            damage = random.randint(10,15)
        print 'You dealt',damage,'damage, and spent 25 MP!'
        enemy.health -= damage
        player.mp -= 25
        print 'MP left:',player.mp
    def evade(self):
        print 'You focus this turn on evading!'
        self.evading = True
    def healthbar(self):
        if self.health == 100:
            print 'Player health left: [//////////]'
        elif self.health >= 90 and self.health < 100:
            print 'Player health left: [/////////-]'
        elif self.health >= 80 and self.health < 90:
            print 'Player health left: [////////--]'
        elif self.health >= 70 and self.health < 80:
            print 'Player health left: [///////---]'
        elif self.health >= 60 and self.health < 70:
            print 'Player health left: [//////----]'
        elif self.health >= 50 and self.health < 60:
            print 'Player health left: [/////-----]'
        elif self.health >= 40 and self.health < 50:
            print 'Player health left: [////------]'
        elif self.health >= 30 and self.health < 40:
            print 'Player health left: [///-------]'
        elif self.health >= 20 and self.health < 30:
            print 'Player health left: [//--------]'
        elif self.health >= 10 and self.health < 20:
            print 'Player health left: [/---------]'
        elif self.health < 10:
            print 'Player health left: [----------]'
class Enemy:
    def __init__(self,health,mp,defending):
        self.health = health
        self.mp = mp
        self.defending = False
    def attack(self):
        print 'You are being attacked!'
        if player.defending == False:
            damage = random.randint(10,15)
        else:
            damage = random.randint(5,8)
        print 'You have been dealt',damage,'damage!'
        player.health -= damage
    def power_attack(self):
        print 'The enemy lunges at you, dealing massive damage!'
        if player.defending == False:
            damage = random.randint(20,30)
        else:
            damage = random.randint(10,20)
        print 'You take',damage,'damage!'
        player.health -= damage
    def heal(self):
        print 'The enemy heals itself!'
        healing = random.randint(10,15)
        self.health += healing
        if self.health > 100:
            self.health = 100
        self.mp -= 15
    def defend(self):
        print 'The enemy braces itself!'
        self.defending = True
    def healthbar(self):
        if enemy_select == 1:
                if self.health == 100:
                    print 'Enemy health left:  [//////////]'
                elif self.health >= 90 and self.health < 100:
                    print 'Enemy health left:  [/////////-]'
                elif self.health >= 80 and self.health < 90:
                    print 'Enemy health left:  [////////--]'
                elif self.health >= 70 and self.health < 80:
                    print 'Enemy health left:  [///////---]'
                elif self.health >= 60 and self.health < 70:
                    print 'Enemy health left:  [//////----]'
                elif self.health >= 50 and self.health < 60:
                    print 'Enemy health left:  [/////-----]'
                elif self.health >= 40 and self.health < 50:
                    print 'Enemy health left:  [////------]'
                elif self.health >= 30 and self.health < 40:
                    print 'Enemy health left:  [///-------]'
                elif self.health >= 20 and self.health < 30:
                    print 'Enemy health left:  [//--------]'
                elif self.health >= 10 and self.health < 20:
                    print 'Enemy health left:  [/---------]'
                elif self.health < 10:
                    print 'Enemy health left:  [----------]'
        elif enemy_select == 2:
                if self.health == 60:
                    print 'Enemy health left:  [//////////]'
                elif self.health >= 54 and self.health < 60:
                    print 'Enemy health left:  [/////////-]'
                elif self.health >= 48 and self.health < 54:
                    print 'Enemy health left:  [////////--]'
                elif self.health >= 42 and self.health < 48:
                    print 'Enemy health left:  [///////---]'
                elif self.health >= 36 and self.health < 42:
                    print 'Enemy health left:  [//////----]'
                elif self.health >= 30 and self.health < 36:
                    print 'Enemy health left:  [/////-----]'
                elif self.health >= 24 and self.health < 30:
                    print 'Enemy health left:  [////------]'
                elif self.health >= 18 and self.health < 24:
                    print 'Enemy health left:  [///-------]'
                elif self.health >= 12 and self.health < 18:
                    print 'Enemy health left:  [//--------]'
                elif self.health >= 6 and self.health < 12:
                    print 'Enemy health left:  [/---------]'
                elif self.health < 6:
                    print 'Enemy health left:  [----------]'
        elif enemy_select == 3:
                if self.health == 130:
                    print 'Enemy health left:  [//////////]'
                elif self.health >= 117 and self.health < 130:
                    print 'Enemy health left:  [/////////-]'
                elif self.health >= 104 and self.health < 117:
                    print 'Enemy health left:  [////////--]'
                elif self.health >= 91 and self.health < 104:
                    print 'Enemy health left:  [///////---]'
                elif self.health >= 78 and self.health < 91:
                    print 'Enemy health left:  [//////----]'
                elif self.health >= 65 and self.health < 78:
                    print 'Enemy health left:  [/////-----]'
                elif self.health >= 52 and self.health < 65:
                    print 'Enemy health left:  [////------]'
                elif self.health >= 39 and self.health < 52:
                    print 'Enemy health left:  [///-------]'
                elif self.health >= 26 and self.health < 39:
                    print 'Enemy health left:  [//--------]'
                elif self.health >= 13 and self.health < 26:
                    print 'Enemy health left:  [/---------]'
                elif self.health < 13:
                    print 'Enemy health left:  [----------]'
player = Player(100,100,False,False)
rogue = Enemy(100,100,False)
slime = Enemy(60,0,False)
goblin = Enemy(130,30,False)
enemy_select = random.randint(1,3)
enemy = 0
if enemy_select == 1:
    enemy = rogue
    print 'You encounter a rogue!'
elif enemy_select == 2:
    enemy = slime
    print 'You encounter a slime!'
elif enemy_select == 3:
    enemy = goblin
    print 'You encounter a goblin!'
while player.health >= 0 and enemy.health >= 0:

    if player.health <=0:
        break

    option = raw_input("What would you like to do? (Type help for command list) ")
    if option == 'status':
        player.status()
        continue
    elif option == 'defend':
        player.defend()
    elif option == 'attack':
        if random.randint(1,10) == 1:
            print 'You tried to attack, but you missed!'
        else:
            player.attack()
    elif option == 'heal':
        if player.mp >= 10:
            player.heal()
        else:
            print "You don't have enough MP!"
            continue
    elif option == 'power attack':
        if player.mp >= 25:
            if random.randint(1,10) == 1:
                print 'You imbue your sword with magic, but you take too long and the enemy sees your attack coming!'
                player.mp -= 25
            else:
                player.power_attack()
        else:
            print "You don't have enough MP!"
            continue
    elif option == 'help':
        print 'status: Check on your current HP and MP'
        print 'attack: Deal damage to the enemy'
        print 'defend: Use your turn to take half damage from the enemy, if it attacks'
        print 'evade: Use your turn to increase the chances for the enemy to miss their attack for that turn'
        print 'heal: use 10 MP to heal yourself 15-20 HP'
        print 'power attack: use 25 MP to deal 20-30 damage to the enemy'
        continue
    elif option == 'evade':
        player.evade()
    else:
        print 'Invalid option.'
        continue
    if enemy.health <=0:
        break
    enemy.defending = False
    enemy_choice = random.randint(1,4)
    if enemy_choice == 1:
        if player.evading == True and random.randint(1,5) == 1:
            print 'The enemy tried to attack, but it missed!'
        elif player.evading == False and random.randint(1,10) == 1:
            print 'The enemy tried to attack, but it missed!'
        else:
            enemy.attack()
    elif enemy_choice == 2:
        magic = random.randint(1,4)
        if enemy_select == 1:
            if enemy.health <= 50:
                if magic == 1 or enemy.mp < 15:
                    enemy.power_attack()
                else:
                    enemy.heal()
            else:
                if player.evading == True and random.randint(1,5) == 1:
                    print 'The enemy tried to attack, but it missed!'
                elif player.evading == False and random.randint(1,10) == 1:
                    print 'The enemy tried to attack, but it missed!'
                else:
                    enemy.power_attack()
        elif enemy_select == 2:
            if enemy.health <= 30:
                if magic == 1 or enemy.mp < 15:
                    enemy.power_attack()
                else:
                    enemy.heal()
            else:
                if player.evading == True and random.randint(1,5) == 1:
                    print 'The enemy tried to attack, but it missed!'
                elif player.evading == False and random.randint(1,10) == 1:
                    print 'The enemy tried to attack, but it missed!'
                else:
                    enemy.power_attack()
        elif enemy_select == 3:
            if enemy.health <= 65:
                if magic == 1 or enemy.mp < 15:
                    enemy.power_attack()
                else:
                    enemy.heal()
            else:
                if player.evading == True and random.randint(1,5) == 1:
                    print 'The enemy tried to attack, but it missed!'
                elif player.evading == False and random.randint(1,10) == 1:
                    print 'The enemy tried to attack, but it missed!'
                else:
                    enemy.power_attack()
    elif enemy_choice == 3:
        enemy.heal()
    elif enemy_choice == 4:
        enemy.defend()
    player.defending = False
    player.evading = False
    player.healthbar()
    enemy.healthbar()
if player.health <= 0:
    print 'You have lost!'
if enemy.health <= 0:
    print 'You won!'
print 'You earned',random.randint(500,600),'EXP!'
raw_input('Press enter to close.')

import random,sys,time,functions
print_slow = functions.print_slow
class Player:
    def __init__(self,max_health,max_mp,health,mp,damage_bonus,defending,evading,EXP,level_EXP):
        self.max_health = max_health
        self.max_mp = max_mp
        self.health = health
        self.mp = mp
        self.damage_bonus = damage_bonus
        self.defending = False
        self.evading = False
        self.EXP = EXP
        self.level_EXP = level_EXP
    def status(self):
        print 'HP:',self.health
        print 'MP:',self.mp
    def attack(self):
        print_slow('You attack!\n')
        if enemy.defending == False:
            damage = self.damage_bonus + random.randint(10,15)
        else:
            damage = self.damage_bonus + random.randint(5,8)
        print_slow('You dealt '+str(damage)+' damage!\n')
        enemy.health -= damage
    def defend(self):
        print_slow('You brace yourself!\n')
        self.defending = True
    def heal(self):
        print_slow('You heal yourself!\n')
        healing = random.randint(15,20)
        player.health += healing
        if player.health > player.max_health:
            player.health = player.max_health
        player.mp -= 10
        print_slow('You healed '+str(healing)+' HP, leaving you with '+str(player.health)+' health and '+str(player.mp)+' MP left!\n')
    def power_attack(self):
        print_slow('You imbue your sword with magic and lunge at the enemy!\n')
        if enemy.defending == False:
            damage = self.damage_bonus + random.randint(20,30)
        else:
            damage = self.damage_bonus + random.randint(10,15)
        print_slow('You dealt '+str(damage)+' damage, and spent 25 MP!\n')
        enemy.health -= damage
        player.mp -= 25
        print_slow('MP left: '+str(player.mp)+'\n')
    def evade(self):
        print_slow('You focus this turn on evading!\n')
        self.evading = True
    def healthbar(self):
        if self.health == 100:
            print_slow('Player health left: [//////////]\n')
        elif self.health >= 90 and self.health < 100:
            print_slow('Player health left: [/////////-]\n')
        elif self.health >= 80 and self.health < 90:
            print_slow('Player health left: [////////--]\n')
        elif self.health >= 70 and self.health < 80:
            print_slow('Player health left: [///////---]\n')
        elif self.health >= 60 and self.health < 70:
            print_slow('Player health left: [//////----]\n')
        elif self.health >= 50 and self.health < 60:
            print_slow('Player health left: [/////-----]\n')
        elif self.health >= 40 and self.health < 50:
            print_slow('Player health left: [////------]\n')
        elif self.health >= 30 and self.health < 40:
            print_slow('Player health left: [///-------]\n')
        elif self.health >= 20 and self.health < 30:
            print_slow('Player health left: [//--------]\n')
        elif self.health >= 10 and self.health < 20:
            print_slow('Player health left: [/---------]\n')
        elif self.health < 10:
            print_slow('Player health left: [----------]\n')
    def inventory(self):
        print '[1] Health Potion: Heal 50 HP. In inventory:',health_potion.in_inventory
        print '[2] Big Health Potion: Heal to full HP. In inventory:',big_health_potion.in_inventory
        print '[3] Mana Potion: Recover 50 MP. In inventory:',mana_potion.in_inventory
        print '[4] Big Mana Potion: Heal to full MP. In inventory:',big_mana_potion.in_inventory
        print '[5] Firecracker: Deal 20 damage to the enemy. In inventory:',firecracker.in_inventory
        print '[6] Bomb: Deal 60 damage to the enemy. In inventory:',bomb.in_inventory
        print '[0] Go back to the action menu'
    def level_up(self):
        print_slow('You leveled up! Maximum health and mana increased by 10. Damage increased by 5!\n')
        self.max_health += 10
        self.max_mp += 10
        self.damage_bonus += 5
        self.level_EXP += 500
class Enemy:
    def __init__(self,health,mp,defending):
        self.health = health
        self.mp = mp
        self.defending = False
    def attack(self):
        print_slow('You are being attacked!\n')
        if player.defending == False:
            damage = random.randint(10,15)
        else:
            damage = random.randint(5,8)
        print_slow('You have been dealt '+str(damage)+' damage!\n')
        player.health -= damage
    def power_attack(self):
        print_slow('The enemy lunges at you, dealing massive damage!\n')
        if player.defending == False:
            damage = random.randint(20,30)
        else:
            damage = random.randint(10,20)
        print_slow('You take '+str(damage)+' damage!\n')
        player.health -= damage
    def heal(self):
        print_slow('The enemy heals itself!\n')
        healing = random.randint(10,15)
        self.health += healing
        if self.health > 100:
            self.health = 100
        self.mp -= 15
    def defend(self):
        print_slow('The enemy braces itself!\n')
        self.defending = True
    def healthbar(self):
        if enemy_select == 1:
                if self.health == 100:
                    print_slow('Enemy health left:  [//////////]\n')
                elif self.health >= 90 and self.health < 100:
                    print_slow('Enemy health left:  [/////////-]\n')
                elif self.health >= 80 and self.health < 90:
                    print_slow('Enemy health left:  [////////--]\n')
                elif self.health >= 70 and self.health < 80:
                    print_slow('Enemy health left:  [///////---]\n')
                elif self.health >= 60 and self.health < 70:
                    print_slow('Enemy health left:  [//////----]\n')
                elif self.health >= 50 and self.health < 60:
                    print_slow('Enemy health left:  [/////-----]\n')
                elif self.health >= 40 and self.health < 50:
                    print_slow('Enemy health left:  [////------]\n')
                elif self.health >= 30 and self.health < 40:
                    print_slow('Enemy health left:  [///-------]\n')
                elif self.health >= 20 and self.health < 30:
                    print_slow('Enemy health left:  [//--------]\n')
                elif self.health >= 10 and self.health < 20:
                    print_slow('Enemy health left:  [/---------]\n')
                elif self.health < 10:
                    print_slow('Enemy health left:  [----------]\n')
        elif enemy_select == 2:
                if self.health == 60:
                    print_slow('Enemy health left:  [//////////]\n')
                elif self.health >= 54 and self.health < 60:
                    print_slow('Enemy health left:  [/////////-]\n')
                elif self.health >= 48 and self.health < 54:
                    print_slow('Enemy health left:  [////////--]\n')
                elif self.health >= 42 and self.health < 48:
                    print_slow('Enemy health left:  [///////---]\n')
                elif self.health >= 36 and self.health < 42:
                    print_slow('Enemy health left:  [//////----]\n')
                elif self.health >= 30 and self.health < 36:
                    print_slow('Enemy health left:  [/////-----]\n')
                elif self.health >= 24 and self.health < 30:
                    print_slow('Enemy health left:  [////------]\n')
                elif self.health >= 18 and self.health < 24:
                    print_slow('Enemy health left:  [///-------]\n')
                elif self.health >= 12 and self.health < 18:
                    print_slow('Enemy health left:  [//--------]\n')
                elif self.health >= 6 and self.health < 12:
                    print_slow('Enemy health left:  [/---------]\n')
                elif self.health < 6:
                    print_slow('Enemy health left:  [----------]\n')
        elif enemy_select == 3:
                if self.health == 130:
                    print_slow('Enemy health left:  [//////////]\n')
                elif self.health >= 117 and self.health < 130:
                    print_slow('Enemy health left:  [/////////-]\n')
                elif self.health >= 104 and self.health < 117:
                    print_slow('Enemy health left:  [////////--]\n')
                elif self.health >= 91 and self.health < 104:
                    print_slow('Enemy health left:  [///////---]\n')
                elif self.health >= 78 and self.health < 91:
                    print_slow('Enemy health left:  [//////----]\n')
                elif self.health >= 65 and self.health < 78:
                    print_slow('Enemy health left:  [/////-----]\n')
                elif self.health >= 52 and self.health < 65:
                    print_slow('Enemy health left:  [////------]\n')
                elif self.health >= 39 and self.health < 52:
                    print_slow('Enemy health left:  [///-------]\n')
                elif self.health >= 26 and self.health < 39:
                    print_slow('Enemy health left:  [//--------]\n')
                elif self.health >= 13 and self.health < 26:
                    print_slow('Enemy health left:  [/---------]\n')
                elif self.health < 13:
                    print_slow('Enemy health left:  [----------]\n')
class Item:
    def __init__ (self,hp_recovery,mp_recovery,item_damage,in_inventory):
        self.hp_recovery = hp_recovery
        self.mp_recovery = mp_recovery
        self.item_damage = item_damage
        self.in_inventory = in_inventory
    def consume(self):
        if self.hp_recovery > 0:
            print_slow('You healed '+str(self.hp_recovery)+' HP with your item!\n')
            player.health += self.hp_recovery
            if player.health > player.max_health:
                player.health = player.max_health
            self.in_inventory -= 1
        elif self.mp_recovery > 0:
            print_slow('You recovered '+str(self.mp_recovery)+' MP with your item!\n')
            player.health += mp_recovery
            if player.mp > player.max_mp:
                player.mp = player.max_mp
            self.in_inventory -= 1
        elif self.item_damage > 0:
            print_slow('You dealt '+str(self.item_damage)+' damage with your item!\n')
            enemy.health -= self.item_damage
            self.in_inventory -= 1
    def restock(self):
        health_potion.in_inventory += 1
        big_health_potion.in_inventory += 1
        mana_potion.in_inventory += 1
        big_mana_potion.in_inventory += 1
        firecracker.in_inventory += 1
        bomb.in_inventory += 1
player = Player(100,100,100,100,0,False,False,0,500)
rogue = Enemy(100,100,False)
slime = Enemy(60,0,False)
goblin = Enemy(130,30,False)
health_potion = Item(50,0,0,3)
big_health_potion = Item(100,0,0,1)
mana_potion = Item(0,50,0,3)
big_mana_potion = Item(0,100,0,1)
firecracker = Item(0,0,20,3)
bomb = Item(0,0,60,1)
bag = Item(0,0,0,0)
doomsday = Item(0,0,1000,1)
while True:
    enemy_select = random.randint(1,3)
    if enemy_select == 1:
        enemy = rogue
        print_slow('You encounter a rogue!\n')
    elif enemy_select == 2:
        enemy = slime
        print_slow('You encounter a slime!\n')
    elif enemy_select == 3:
        enemy = goblin
        print_slow('You encounter a goblin!\n')
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
                print_slow('You tried to attack, but you missed!\n')
            else:
                player.attack()
        elif option == 'heal':
            if player.mp >= 10:
                player.heal()
            else:
                print_slow("You don't have enough MP!\n")
                continue
        elif option == 'power attack':
            if player.mp >= 25:
                if random.randint(1,10) == 1:
                    print_slow('You imbue your sword with magic, but you take too long and the enemy sees your attack coming!\n')
                    player.mp -= 25
                else:
                    player.power_attack()
            else:
                print_slow("You don't have enough MP!\n")
                continue
        elif option == 'help':
            print 'status: Check on your current HP and MP'
            print 'attack: Deal damage to the enemy'
            print 'defend: Use your turn to take half damage from the enemy, if it attacks'
            print 'inventory: Check your bag for items, details inside the menu'
            print 'evade: Use your turn to increase the chances for the enemy to miss their attack for that turn'
            print 'heal: use 10 MP to heal yourself 15-20 HP'
            print 'power attack: use 25 MP to deal 20-30 damage to the enemy'
            continue
        elif option == 'evade':
            player.evade()
        elif option == 'inventory':
            player.inventory()
            item_choice = input('Enter your choice: ')
            if item_choice == 1:
                health_potion.consume()
            elif item_choice == 2:
                big_health_potion.consume()
            elif item_choice == 3:
                mana_potion.consume()
            elif item_choice == 4:
                big_mana_potion.consume()
            elif item_choice == 5:
                firecracker.consume()
            elif item_choice == 6:
                bomb.consume()
            elif item_choice == 69:
                doomsday.consume()
            else:
                continue
        else:
            print 'Invalid option.'
            continue
        if enemy.health <=0:
            break
        enemy.defending = False
        enemy_choice = random.randint(1,4)
        if enemy_choice == 1:
            if player.evading == True and random.randint(1,5) == 1:
                print_slow('The enemy tried to attack, but it missed!\n')
            elif player.evading == False and random.randint(1,10) == 1:
                print_slow('The enemy tried to attack, but it missed!\n')
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
                        print_slow('The enemy tried to attack, but it missed!\n')
                    elif player.evading == False and random.randint(1,10) == 1:
                        print_slow('The enemy tried to attack, but it missed!\n')
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
                        print_slow('The enemy tried to attack, but it missed!\n')
                    elif player.evading == False and random.randint(1,10) == 1:
                        print_slow('The enemy tried to attack, but it missed!\n')
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
                        print_slow('The enemy tried to attack, but it missed!\n')
                    elif player.evading == False and random.randint(1,10) == 1:
                        print_slow('The enemy tried to attack, but it missed!\n')
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
        print_slow('You have lost!\n')
        break
    if enemy.health <= 0:
        print_slow ('You won!\n')
        EXP_earned = random.randint(500,600)
        print_slow('You earned '+str(EXP_earned)+' EXP!\n')
        player.EXP += EXP_earned
        if player.EXP >= player.level_EXP:
            player.EXP -= player.level_EXP
            player.level_up()
        bag.restock()
        player.health = player.max_health
        player.mp = player.max_mp
        if enemy_select == 1:
            enemy.health = 100
            enemy.mp = 100
        elif enemy_select == 2:
            enemy.health = 60
            enemy.mp = 0
        elif enemy_select == 3:
            enemy.health = 130
            enemy.mp = 30

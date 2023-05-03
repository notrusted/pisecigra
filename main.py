import pygame
from random import randint

bonus_attack = 0
flag_ability = 1
#проверка на подключение к паблик проекту
#Mega test
#мега проверка
#мега проверка 20
#мега проверка 26
#супер проверка 27
class Character:
    def __init__(self,Hp, Strong, Ability, Weapon):
        self.strong = Strong
        self.hp = Hp
        self.ability = Ability
        self.weapon = Weapon

    def Attack(self):
        return (self.strong + self.weapon.damage)

    def Protect(self):
        print('Try to Protect')
        print()

    def Use_the_Ability(self):
        print("use ability: ", self.ability)
        print()


class Elf(Character):

    def __init__(self):
        Character.__init__(self,90,30, "has agility",Weapon("Bow",30))


    def Attack(self):
        print("The Elf attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a =  5 * randint(0,1)
        self.hp = self.hp + a
        print("The Elf's protect give him a " + str(a) + " Hp")

    def Use_the_Ability(self):
        global flag_ability,Arrow_How
        if flag_ability != 0:
            print("The Elf try to use him agility")
            Arrow_How += 15
        flag_ability = 0



class Human(Character):

    def __init__(self):
        Character.__init__(self,150,40, "is a tracker", Weapon("sword", 15))

    def Attack(self):
        global bonus_attack
        print("The Human attack with damage", self.strong + bonus_attack + self.weapon.damage)
        a = self.strong + bonus_attack + self.weapon.damage
        bonus_attack = 0
        return a

    def Protect(self):
        a = randint(0, 1)
        self.hp = self.hp + a * 15
        print("the Human's protect give him a  " + str(a * 15) + " Hp")

    def Use_the_Ability(self):
        global flag_ability, bonus_attack
        if flag_ability != 0:
            print('The Human Find the vulnerability')
            bonus_attack += randint(20,35)
        flag_ability = 0

class Hobbit(Character):

    def __init__(self):
        Character.__init__(self,50,70, 'can a hide', Weapon('Arnors knife', 15))

    def Attack(self):
        print( "The Hobbit attack with damage", self.strong + self.weapon.damage)
        return self.strong + self.weapon.damage

    def Protect(self):
        a = randint(0,1) * randint(1,5) * 5
        self.hp = self.hp + a
        print("The Hobbit's  protect give him a " + str(a) +' Hp')

    def Use_the_Ability(self):
        global flag_ability
        if flag_ability != 0:
            print( " The Hobbit was able to hide")
            self.hp += 15
        flag_ability = 0






class Weapon:
    def __init__(self, Name, Damage):
        self.name = Name
        self.damage = Damage



class Monster:
    def __init__(self, Hp, Armor, X,Y, Damage, Weapon):
        self.hp = Hp
        self.armor = Armor
        self.damage = Damage
        self.weapon = Weapon
        self.x = X
        self.y = Y

    def Attack(self):
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        a = randint(0, 1)
        self.hp = self.hp - dmg + dmg * a * a


class Nazgul(Monster):
    def __init__(self):
        Monster.__init__(self, randint(20, 50),  randint(5, 20), 250,-100,randint(1,15),Weapon("Morgul's knife",randint(5,10)))


    def Attack(self):
        print('Nazgul attack with damage', self.damage + self.weapon.damage)
        return self.damage + self.weapon.damage

    def Protect(self, dmg):
        print('Nazgul try to protect')
        b = dmg
        self.hp = self.hp - dmg + (b * randint(0, 1) * randint(0, 1))






clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("The Hobbit: Pyton's Adventure")
#icon = pygame.image.load("I-ICON.png")
#pygame.display.set_icon(icon)

bg = pygame.image.load("images/Back.png")
#player = pygame.image.load("I-ICON.png")

Walk_right = [pygame.image.load('images/Right-1.png'),pygame.image.load('images/Right-2.png')]
Walk_left  = [pygame.image.load('images/Left-1.png'),pygame.image.load('images/Left-2.png')]
Walk_Up = [pygame.image.load('images/Up-1.png'),pygame.image.load("images/Up-2.png")]
Walk_Down = [pygame.image.load('images/Down_-_1.png'),pygame.image.load('images/Down-2.png')]

Nazgul_right = [pygame.image.load("images/Nazgul-2-1.png"),pygame.image.load("images/Nazgul-2-1-right-eyes.png")]
Nazgul_left = [pygame.image.load("images/Nazgul-2-1-left.png"),pygame.image.load("images/Nazgul-2-1-left-eyes.png")]
Nazgul_attack_left = pygame.image.load("images/Nazgul-3-left.png")
Nazgul_attack_right = pygame.image.load("images/Nazgul-3-rigt.png")



n_flag = True
n_timer = pygame.USEREVENT + 1
pygame.time.set_timer(n_timer,10000)
n_list_it_the_game = []
n_animation_count = 0


Player_animation_count = 0
bg_y = 0



player_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf",30)



player_speed = 15
player_x = 300
player_y = 250
flag_animation = True
Type_anim = 0

gameplay = True
the_end_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf",50)
loose_label = the_end_label.render('You died',False,(12,12,12))
restart_label = the_end_label.render("Start again",False,(35,234,32))
restart_label_rect = restart_label.get_rect(topleft = (250,400))



Arrow = pygame.image.load("images/Arrow.png")
Arrow_list = []
Arrow_How = 0
Arrow_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf",20)
Attack_point = 0


Start_game_flag = True
entr = False


running = True
while running:

    if Start_game_flag :
        gameplay = False
        screen.fill("Black")
        label = pygame.font.Font('fonts/RobotoMono-VariableFont_wght.ttf',20)
        Game_Name = label.render("The Hobbit: Pyton's Adventure",False,"Yellow")
        screen.blit(Game_Name,(250,400))
        Game_start = label.render("Press any to start...",False,"Yellow")
        screen.blit(Game_start,(250,600))

        if entr:
            screen.fill("Black")
            Character_label = label.render("Choose your hero:",False,"Red")
            screen.blit(Character_label,(250,200))
            Character_label_Elf = label.render("Forest Elf",False,"Yellow")
            screen.blit(Character_label_Elf,(250,400))
            Character_label_Human = label.render("Human", False, "Yellow")
            screen.blit(Character_label_Human, (250, 500))
            Character_label_Hobbit = label.render("Hobbit", False, "Yellow")
            screen.blit(Character_label_Hobbit, (250, 600))

            Character_label_Elf_rect = Character_label_Elf.get_rect(topleft = (250,400))
            Character_label_Human_rect = Character_label_Human.get_rect(topleft=(250,500))
            Character_label_Hobbit_rect = Character_label_Hobbit.get_rect(topleft=(250, 600))

            mouse = pygame.mouse.get_pos()
            if Character_label_Elf_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Elf")
                player_character = Elf()
                All_Hp = player_character.hp
                Arrow_How = 100
                Start_game_flag = False

            elif Character_label_Human_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Human")
                player_character = Human()
                All_Hp = player_character.hp
                Start_game_flag = False

            elif Character_label_Hobbit_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
                gameplay = True
                print("Your choose is Hobbit")
                player_character = Hobbit()
                All_Hp = player_character.hp
                Start_game_flag = False



    if gameplay :
        screen.blit(bg, (0, bg_y))
        screen.blit(bg, (0, bg_y - 800))
        if player_character.ability == "has agility":
            Arrow_label_how = Arrow_label.render("You have a " + str(Arrow_How) + " arrow's", False, "Brown")
            Arrow_label_press = Arrow_label.render("Press R...",False,"Brown")
            Character_label_Elf_ability = Arrow_label.render("You can" + (1 - flag_ability) *"'t" + " use " +"The ability: " + str(player_character.ability),False,'Brown')
            screen.blit(Arrow_label_how, (700, 30))
            screen.blit(Arrow_label_press,(700,60))
            screen.blit(Character_label_Elf_ability,(500,750))

        else:
            Arrow_label_how = Arrow_label.render("You can touch with  " + str(player_character.weapon.name), False, "Brown")
            Arrow_label_press = Arrow_label.render("Press F...", False, "Brown")
            Character_label_Hobbit_and_Human_ability = Arrow_label.render(
                "You can" + (1 - flag_ability) * "'t" + " use " + "The ability: " + str(player_character.ability),
                False, 'Brown')
            screen.blit(Arrow_label_how, (600, 30))
            screen.blit(Arrow_label_press, (600, 60))
            screen.blit(Character_label_Hobbit_and_Human_ability, (500, 750))


        if n_list_it_the_game:
            for (i,elem) in enumerate (n_list_it_the_game):
                n_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
                n_heal_points = n_label.render("Hp: " + str(elem.hp),False,"green")
                n_armor = n_label.render("Armor: " + str(elem.armor),False,"green")

                if (abs(elem.x - player_x) <= 200) and (abs(elem.y - player_y) <= 200):

                    if elem.x >= player_x:
                        screen.blit(Nazgul_attack_left, (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor,(elem.x + 10, elem.y - 60))
                    if elem.x < player_x:
                        screen.blit(Nazgul_attack_right, (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))
                    n_flag = False

                else:
                    n_flag = True

                if elem.x < player_x:
                    elem.x += 2
                    if n_flag:
                        if n_animation_count == 1:
                            n_animation_count = 0
                        else:
                            n_animation_count += 1
                        screen.blit(Nazgul_right[n_animation_count], (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))

                if elem.x > player_x:
                    elem.x -= 2
                    if n_flag:
                        if n_animation_count == 1:
                            n_animation_count = 0
                        else:
                            n_animation_count += 1
                        screen.blit(Nazgul_left[n_animation_count], (elem.x, elem.y))
                        screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                        screen.blit(n_armor, (elem.x + 10, elem.y - 60))

                if elem.y < player_y:
                    elem.y += 2

                if elem.y > player_y:
                    elem.y -= 2

                if abs(elem.x - player_x) < 50 and abs(elem.y  - player_y) < 50:
                    player_character.hp -= elem.Attack()
                    player_y += 150
                    if player_character.hp <= 0:
                        player_character.hp = 0
                        gameplay = False



        if flag_animation:
            player_heal_points = player_label.render("Hp: " + str(player_character.hp), False, "Red")
            if Type_anim == 0:
                screen.blit(Walk_Up[0], (player_x, player_y))
                screen.blit(player_heal_points,(player_x + 20,player_y - 30))
            elif Type_anim == 1:
                screen.blit(Walk_left[0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))
            elif Type_anim == 2:
                screen.blit(Walk_right[0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))
            elif Type_anim == 3:
                screen.blit(Walk_Down[0], (player_x, player_y))
                screen.blit(player_heal_points, (player_x + 20, player_y - 30))

        flag_animation = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and player_x < 800:
            screen.blit(Walk_right[Player_animation_count], (player_x, player_y))
            player_x += player_speed
            flag_animation = False
            Type_anim = 2



        elif keys[pygame.K_a] and player_x > 0:
            screen.blit(Walk_left[Player_animation_count], (player_x, player_y))
            player_x -= player_speed
            flag_animation = False
            Type_anim = 1



        elif keys[pygame.K_w]:
            screen.blit(Walk_Up[Player_animation_count], (player_x, player_y))
            player_y -= player_speed
            bg_y += 2
            Type_anim = 0
            flag_animation = False
            if player_y < -200:
                player_y = 690

        elif keys[pygame.K_s] and player_y < 700:
            screen.blit(Walk_Down[Player_animation_count], (player_x, player_y))
            player_y += player_speed
            bg_y -= 2
            Type_anim = 3
            flag_animation = False

        if Player_animation_count == 1:
            Player_animation_count = 0

        else:
            Player_animation_count += 1

        if bg_y == 800:
            bg_y = 0

        elif bg_y < 0:
            bg_y = 0


        if Arrow_list:
            for (i,ar) in enumerate( Arrow_list):
                screen.blit(Arrow,(ar.x,ar.y))
                ar.y -= 20

                if n_list_it_the_game:
                    for (j,elem) in enumerate( n_list_it_the_game):
                        if abs(ar.x - elem.x) < 100 and abs(ar.y - elem.y) < 100:
                            elem.y -= 50

                            if elem.armor > 0:
                                elem.armor -= Attack_point
                                if elem.armor < 0:
                                    elem.armor = 0
                            else:
                                elem.Protect(Attack_point)

                            if elem.hp <= 0:
                                n_list_it_the_game.pop(j)
                                print("the Nazgul is murdered...")
                                flag_ability = 1

                            if Arrow_list:
                              Arrow_list.pop(i)


                        if Arrow_list:
                           if ar.y < -100:
                              Arrow_list.pop(i)





    elif Start_game_flag == False:
        screen.fill("White")
        screen.blit(loose_label,(250,500))
        screen.blit(restart_label,(250,400))
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed():
            player_y = 500
            n_list_it_the_game.clear()
            Arrow_list.clear()
            player_character.hp = All_Hp
            flag_ability = 1
            Arrow_How = 0
            Start_game_flag = True


    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False
            pygame.quit()

        if event.type == n_timer:
            n_list_it_the_game.append(Nazgul())

        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_r and Arrow_How > 0 and player_character.ability == "has agility":
            Arrow_list.append(Arrow.get_rect(topleft=(player_x, player_y - 30)))
            Arrow_How -= 1
            Attack_point = player_character.Attack()

        if Start_game_flag and event.type == pygame.KEYDOWN:
            entr = True

        if gameplay and (player_character.ability == "is a tracker" or player_character.ability == "can a hide") and event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            a = player_character.Attack()
            if Attack_point <= a:
                Attack_point = a
            if n_list_it_the_game:
                for (j,elem) in enumerate(n_list_it_the_game):
                    if abs(elem.x - player_x) < 70 and abs(elem.y - player_y) < 70:
                        elem.y -= 100

                        if elem.armor > 0:
                            elem.armor -= Attack_point
                            if elem.armor < 0:
                                elem.armor = 0
                        else:
                            elem.Protect(Attack_point)

                        Attack_point = 0

                        if elem.hp <= 0:
                            n_list_it_the_game.pop(j)
                            print("the Nazgul is murdered...")
                            flag_ability = 1

        if gameplay and event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            player_character.Use_the_Ability()



    clock.tick(20)



import pygame

from file_for_images import Boss_warg_Heal, Boss_warg_Left, Boss_warg_Right, Boss_warg_Up, Boss_warg_Down, Warg_Left, \
    Warg_Up, Warg_Right, Warg_Down, Nazgul_left, Nazgul_right, Nazgul_attack, Orc_down, Orc_up, Orc_right, Orc_left, \
    boss_nazgul_down


class Mechanics_of_Mobs():
    def __init__(self,gameplay,player,screen):
        self.gameplay = gameplay
        self.player = player
        self.screen = screen

    def orc_mechanicks_go(self,orc_list_in_the_game,orc_flag,Character,player_x, player_y):
        if orc_list_in_the_game:

            for (i, elem) in enumerate(orc_list_in_the_game):
                orc_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
                orc_heal_points = orc_label.render("Hp: " + str(elem.hp), False, "green")
                orc_armor = orc_label.render("Armor: " + str(elem.armor), False, "green")

                if abs(elem.x - player_x) <= 60 and abs(elem.y - player_y) <= 60:
                    self.player.hp -= elem.Attack()
                    player_y += 150
                    if self.player.hp <= 0:
                        self.player.hp = 0
                        self.gameplay = False

                elif Character.pred_rsp_hero[0] == player_x and player_y == Character.pred_rsp_hero[1]:
                    if abs(elem.x - player_x) > 5:
                        orc_flag += 1
                        if elem.x > player_x:
                            elem.x -= 4
                            elem.anim += 1
                            self.screen.blit(Orc_left[elem.anim % 3], (elem.x, elem.y))
                            self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                            self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                        else:
                            elem.x += 4
                            elem.anim += 1
                            self.screen.blit(Orc_right[elem.anim % 3], (elem.x, elem.y))
                            self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                            self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                    else:
                        orc_flag = 0
                        if elem.y > player_y:
                            elem.y -= 4
                            elem.anim += 1
                            self.screen.blit(Orc_up[elem.anim % 3], (elem.x, elem.y))
                            self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                            self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                        else:
                            elem.y += 4
                            elem.anim += 1
                            self.screen.blit(Orc_down[elem.anim % 3], (elem.x, elem.y))
                            self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                            self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))


                elif abs(elem.x - player_x) > abs(elem.y - player_y):
                    orc_flag += 1
                    if elem.x > player_x:
                        elem.x -= 4
                        elem.anim += 1
                        self.screen.blit(Orc_left[elem.anim % 3], (elem.x, elem.y))
                        self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                        self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                    else:
                        elem.x += 4
                        elem.anim += 1
                        self.screen.blit(Orc_right[elem.anim % 3], (elem.x, elem.y))
                        self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                        self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                elif abs(elem.x - player_x) <= abs(elem.y - player_y):
                    orc_flag = 0
                    if elem.y > player_y:
                        elem.y -= 4
                        elem.anim += 1
                        self.screen.blit(Orc_up[elem.anim % 3], (elem.x, elem.y))
                        self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                        self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
                    else:
                        elem.y += 4
                        elem.anim += 1
                        self.screen.blit(Orc_down[elem.anim % 3], (elem.x, elem.y))
                        self.screen.blit(orc_heal_points, (elem.x + 10, elem.y - 30))
                        self.screen.blit(orc_armor, (elem.x + 10, elem.y - 60))
        x = self.player.Player_coordinate()

    def nazgul_mechanicks_go(self,n_list_it_the_game, n_flag,player_x, player_y):
        for (i, elem) in enumerate(n_list_it_the_game):
            n_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
            n_heal_points = n_label.render("Hp: " + str(elem.hp), False, "green")
            n_armor = n_label.render("Armor: " + str(elem.armor), False, "green")

            if (abs(elem.x - player_x) <= 200) and (abs(elem.y - player_y) <= 200):

                if elem.x >= player_x:
                    self.screen.blit(Nazgul_attack[0], (elem.x, elem.y))
                    self.screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                    self.screen.blit(n_armor, (elem.x + 10, elem.y - 60))
                if elem.x < player_x:
                    self.screen.blit(Nazgul_attack[1], (elem.x, elem.y))
                    self.screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                    self.screen.blit(n_armor, (elem.x + 10, elem.y - 60))
                n_flag = False

            else:
                n_flag = True

            if elem.x - player_x <= 5:
                elem.x += 2
                if n_flag:
                    elem.anim += 1
                    self.screen.blit(Nazgul_right[elem.anim % 2], (elem.x, elem.y))
                    self.screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                    self.screen.blit(n_armor, (elem.x + 10, elem.y - 60))

            if elem.x - player_x >= 5:
                elem.x -= 2
                if n_flag:
                    elem.anim += 1
                    self.screen.blit(Nazgul_left[elem.anim % 2], (elem.x, elem.y))
                    self.screen.blit(n_heal_points, (elem.x + 10, elem.y - 30))
                    self.screen.blit(n_armor, (elem.x + 10, elem.y - 60))

            if elem.y - player_y <= 5:
                elem.y += 2

            if elem.y - player_y >= 5:
                elem.y -= 2

            if abs(elem.x - player_x) < 50 and abs(elem.y - player_y) < 50:
                self.player.hp -= elem.Attack()
                player_y += 150
                if self.player.hp <= 0:
                    self.player.hp = 0
                    self.gameplay = False

    def warg_mechanicks_go(self,warg_list_in_the_game,player_x, player_y):

        for (i, elem1) in enumerate(warg_list_in_the_game):
            warg_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
            warg_heal_points = warg_label.render("Hp: " + str(elem1.hp), False, "green")
            warg_armor = warg_label.render("Armor: " + str(elem1.armor), False, "green")

            if elem1.flag1 and elem1.y <= 1100:
                elem1.y += 15

                elem1.anim += 1
                self.screen.blit(Warg_Down[elem1.anim % 3], (elem1.x, elem1.y))
                self.screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                self.screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

            if elem1.y > 1100 and elem1.flag1:
                a = self.player.Player_coordinate()
                elem1.x = -100
                elem1.y = a[1]
                elem1.flag1 = False
                elem1.flag2 = True

            if elem1.flag2 and elem1.x <= 900:
                elem1.x += 15

                elem1.anim += 1
                self.screen.blit(Warg_Right[elem1.anim % 2], (elem1.x, elem1.y))
                self.screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                self.screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

            if elem1.x > 900 and elem1.flag2:
                a = self.player.Player_coordinate()
                elem1.x = a[0]
                elem1.y = 1100
                elem1.flag2 = False
                elem1.flag3 = True

            if elem1.flag3 and elem1.y >= -100:
                elem1.y -= 15

                elem1.anim += 1
                self.screen.blit(Warg_Up[elem1.anim % 2], (elem1.x, elem1.y))
                self.screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                self.screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

            if elem1.y < -100 and elem1.flag3:
                a = self.player.Player_coordinate()
                elem1.x = 900
                elem1.y = a[1]
                elem1.flag3 = False
                elem1.flag4 = True

            if elem1.flag4 and elem1.x >= -100:
                elem1.x -= 15

                elem1.anim += 1
                self.screen.blit(Warg_Left[elem1.anim % 2], (elem1.x, elem1.y))
                self.screen.blit(warg_heal_points, (elem1.x + 10, elem1.y - 30))
                self.screen.blit(warg_armor, (elem1.x + 10, elem1.y - 60))

            if elem1.x < -100 and elem1.flag4:
                a = self.player.Player_coordinate()
                elem1.x = a[0]
                elem1.y = -100
                elem1.flag4 = False
                elem1.flag1 = True

            if abs(elem1.x - player_x) < 50 and abs(elem1.y - player_y) < 50:
                self.player.hp -= elem1.Attack()

                if player_x > elem1.x:
                    player_x -= 50



                elif player_x < elem1.x:
                    player_x += 50

                if player_y < elem1.y:
                    player_y += 50

                elif player_y > elem1.y:
                    player_y -= 50

                if self.player.hp <= 0:
                    self.player.hp = 0
                    self.gameplay = False

    def Boss_warg_mechanicks_go(self,Boss_warg,player_x,player_y):

        Boss_warg_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
        Boss_warg_name = Boss_warg_label.render("The Alpha Warg", False, "green")
        Boss_warg_heal_points = Boss_warg_label.render("Hp: " + str(Boss_warg.hp), False, "green")
        Boss_warg_armor = Boss_warg_label.render("Armor: " + str(Boss_warg.armor), False, "green")

        if Boss_warg.Boss_warg_Heal_flag == False:
            if Boss_warg.Boss_warg_flag1 and Boss_warg.y <= 1100 and Boss_warg.Boss_warg_Heal_flag == False:
                Boss_warg.y += 20

                Boss_warg.anim += 1
                self.screen.blit(Boss_warg_Down[Boss_warg.anim % 3], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            if Boss_warg.y > 1100 and Boss_warg.Boss_warg_flag1:
                a = self.player.Player_coordinate()
                Boss_warg.x = -100
                Boss_warg.y = a[1]
                Boss_warg.Boss_warg_flag1 = False
                Boss_warg.Boss_warg_flag2 = True

                if Boss_warg.hp <= 100:
                    Boss_warg.Boss_warg_Heal_flag = True
                    pygame.time.set_timer(Boss_warg.timer, 100000000)
                    Boss_warg.armor += 500
                    Boss_warg.x = -100
                    Boss_warg.y = 200

            if Boss_warg.Boss_warg_flag2 and Boss_warg.x <= 900 and Boss_warg.Boss_warg_Heal_flag == False:
                Boss_warg.x += 20

                Boss_warg.anim += 1
                self.screen.blit(Boss_warg_Left[Boss_warg.anim % 2], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            if Boss_warg.x > 900 and Boss_warg.Boss_warg_flag2:
                a = self.player.Player_coordinate()
                Boss_warg.x = a[0]
                Boss_warg.y = 1100
                Boss_warg.Boss_warg_flag2 = False
                Boss_warg.Boss_warg_flag3 = True

                if Boss_warg.hp <= 100:
                    Boss_warg.Boss_warg_Heal_flag = True
                    pygame.time.set_timer(Boss_warg.timer, 100000000)
                    Boss_warg.armor += 500
                    Boss_warg.x = -100
                    Boss_warg.y = 200

            if Boss_warg.Boss_warg_flag3 and Boss_warg.y >= -100 and Boss_warg.Boss_warg_Heal_flag == False:
                Boss_warg.y -= 20

                Boss_warg.anim += 1
                self.screen.blit(Boss_warg_Up[Boss_warg.anim % 2], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            if Boss_warg.y < -100 and Boss_warg.Boss_warg_flag3:
                a = self.player.Player_coordinate()
                Boss_warg.x = 900
                Boss_warg.y = a[1]
                Boss_warg.Boss_warg_flag3 = False
                Boss_warg.Boss_warg_flag4 = True

                if Boss_warg.hp <= 100:
                    Boss_warg.Boss_warg_Heal_flag = True
                    pygame.time.set_timer(Boss_warg.timer, 100000000)
                    Boss_warg.armor += 500
                    Boss_warg.x = -100
                    Boss_warg.y = 200

            if Boss_warg.Boss_warg_flag4 and Boss_warg.x >= -100 and Boss_warg.Boss_warg_Heal_flag == False:
                Boss_warg.x -= 20

                Boss_warg.anim += 1
                self.screen.blit(Boss_warg_Right[Boss_warg.anim % 2], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            if Boss_warg.x < -100 and Boss_warg.Boss_warg_flag4:
                a = self.player.Player_coordinate()
                Boss_warg.x = a[0]
                Boss_warg.y = -100
                Boss_warg.Boss_warg_flag4 = False
                Boss_warg.Boss_warg_flag1 = True

                if Boss_warg.hp <= 100:
                    Boss_warg.Boss_warg_Heal_flag = True
                    pygame.time.set_timer(Boss_warg.timer, 100000000)
                    Boss_warg.armor += 500
                    Boss_warg.x = -100
                    Boss_warg.y = 200

            if abs(Boss_warg.x - player_x) < 50 and abs(Boss_warg.y - player_y) < 50:
                self.player.hp -= Boss_warg.base_attack()

                if player_x > Boss_warg.x:
                    player_x -= 150

                elif player_x < Boss_warg.x:
                    player_x += 150

                if player_y < Boss_warg.y:
                    player_y += 150

                elif player_y > Boss_warg.y:
                    player_y -= 150

                if self.player.hp <= 0:
                    self.player.hp = 0
                    self.gameplay = False

        if Boss_warg.hp > 150:
            Boss_warg.Boss_warg_Heal_flag = False
            Boss_warg.heal_anim = 0
            Boss_warg.Boss_warg_ability_flag = False

        if Boss_warg.Boss_warg_Heal_flag:
            Boss_warg.anim += 1

            if Boss_warg.x < 250:
                Boss_warg.x += 10
                self.screen.blit(Boss_warg_Left[Boss_warg.anim % 2], (Boss_warg.x, Boss_warg.y))
                self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                self.screen.blit(Boss_warg_name, (400, 20))

            else:
                if Boss_warg.heal_anim != 3:
                    self.screen.blit(Boss_warg_Heal[Boss_warg.heal_anim], (Boss_warg.x, Boss_warg.y))
                    self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                    self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                    self.screen.blit(Boss_warg_name, (400, 20))
                    Boss_warg.heal_anim += 1
                else:
                    self.screen.blit(Boss_warg_Heal[3], (Boss_warg.x, Boss_warg.y))
                    self.screen.blit(Boss_warg_heal_points, (Boss_warg.x + 10, Boss_warg.y - 30))
                    self.screen.blit(Boss_warg_armor, (Boss_warg.x + 10, Boss_warg.y - 60))
                    self.screen.blit(Boss_warg_name, (400, 20))
                    Boss_warg.Boss_warg_ability_flag = True


    def Boss_nazgul_mechanicks(self, boss_nazgul):
        Boss_nazgul_label = pygame.font.Font("fonts/RobotoMono-VariableFont_wght.ttf", 25)
        Boss_nazgul_name = Boss_nazgul_label.render("King of nazguls", False, "blue")
        Boss_nazgul_heal_points = Boss_nazgul_label.render("Hp: " + str(boss_nazgul.hp), False, "green")
        Boss_nazgul_armor = Boss_nazgul_label.render("Armor: " + str(boss_nazgul.armor), False, "green")

        #screen.blit(boss_nazgul_down[0],(screen.get_width()//2,200))
        #if duck.x!=1000 or duck.x!=0:
        #    duck.duck_go(screen)
        if boss_nazgul.hp>0:
            self.screen.blit(Boss_nazgul_heal_points, (boss_nazgul.x + 10, boss_nazgul.y - 30))
            self.screen.blit(Boss_nazgul_armor, (boss_nazgul.x + 10, boss_nazgul.y - 60))
            self.screen.blit(Boss_nazgul_name, (400, 20))
            if boss_nazgul.flag_for_proza:
                boss_nazgul.proza(self.screen)
            else:
                if (boss_nazgul.hp>50 or boss_nazgul.flag_magic) and boss_nazgul.flag_invicible==False :
                    boss_nazgul.go_to(self.screen,self.player.Player_coordinate()[0],self.player.Player_coordinate()[1])
                    if abs(self.player.Player_coordinate()[0]-boss_nazgul.x)<25 and abs(self.player.Player_coordinate()[1]-boss_nazgul.y)<25:
                        self.player.hp-=boss_nazgul.standart_attack()
                elif boss_nazgul.hp<=50:
                    boss_nazgul.flag_go_to_center=True
                if boss_nazgul.flag_go_to_center:
                    boss_nazgul.go_to(self.screen,self.screen.get_width()//2,self.screen.get_height()//2)
                    if boss_nazgul.check==True:
                        boss_nazgul.flag_invicible=True
                        boss_nazgul.check=False
                        boss_nazgul.flag_go_to_center=False
                if boss_nazgul.flag_invicible:
                    if boss_nazgul.flag_totem:
                        boss_nazgul.invicible(self.screen)
                        if boss_nazgul.totem_spawn:
                            boss_nazgul.set_totem()
                            #totem_list=[Totem(boss_nazgul.x-200,boss_nazgul.y-200),Totem(boss_nazgul.x-200,boss_nazgul.y+200),Totem(boss_nazgul.x+200,boss_nazgul.y-200),Totem(boss_nazgul.x+200,boss_nazgul.y+200)]
                            boss_nazgul.totem_spawn=False
                        for i in boss_nazgul.totem_list:
                            i.spawn(self.screen)
                            i.draw(self.screen)
                        if boss_nazgul.hp<100 and len(boss_nazgul.totem_list)!=0:
                            if boss_nazgul.flag_heal:
                                boss_nazgul.hp+=5
                                boss_nazgul.flag_heal=False
                                pygame.time.set_timer(boss_nazgul.time_heal,2000)
                        else:
                            boss_nazgul.flag_invicible=False
                            boss_nazgul.totem_list.clear()
                            boss_nazgul.totem_spawn=True
                            boss_nazgul.flag_totem=False
                            pygame.time.set_timer(boss_nazgul.time_totem,20000)
                    else:
                        if not boss_nazgul.flag_magic:
                            if boss_nazgul.flag_create_magic:
                                boss_nazgul.set_magic(boss_nazgul.x,boss_nazgul.y)
                                boss_nazgul.flag_create_magic=False
                            magic=boss_nazgul.get_magic()
                            magic.special_attack(self.screen,self.player.Player_coordinate()[0],self.player.Player_coordinate()[1])
                            self.screen.blit(boss_nazgul_down[0],(boss_nazgul.x,boss_nazgul.y))
                            if abs(magic.x-self.player.Player_coordinate()[0])<=25 and abs(magic.y-self.player.Player_coordinate()[1])<=25:
                                boss_nazgul.flag_magic=True
                                self.player.hp-=magic.damage
                                if self.player.strong>=0:
                                    self.player.strong-=magic.sd
                                    print("Damage reduced by 10 points :( ...")
                                boss_nazgul.flag_invicible=False
                                boss_nazgul.flag_magic=True
                if self.player.hp <= 0:
                    self.player.hp = 0
                    self.gameplay = False

    def visual_health(self,health_model, Fullhp):

        health = self.player.hp
        section = Fullhp // 9
        level_hp = health // section
        if level_hp == 9:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[0], (150, 50))
            self.screen.blit(health_model[0], (200, 50))
        elif level_hp == 8:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[0], (150, 50))
            self.screen.blit(health_model[1], (200, 50))
        elif level_hp == 7:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[0], (150, 50))
            self.screen.blit(health_model[2], (200, 50))
        elif level_hp == 6:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[0], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 5:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[1], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 4:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[2], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 3:
            self.screen.blit(health_model[0], (100, 50))
            self.screen.blit(health_model[2], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 2:
            self.screen.blit(health_model[1], (100, 50))
            self.screen.blit(health_model[2], (150, 50))
            self.screen.blit(health_model[2], (200, 50))

        elif level_hp == 1 or health > 0:
            self.screen.blit(health_model[2], (100, 50))
            self.screen.blit(health_model[2], (150, 50))
            self.screen.blit(health_model[2], (200, 50))
import pygame
from sources import default,tools,setup
from states import roles,goods,load_js,npc,chat_board,items_interation

class Cpt4:
    '''
        this is chapter one code
    '''
    def __init__(self):
        self.state_name = 'cpt4'
        self.Cpt1_background()
        self.setup_role()
        self.setup_npc()
        self.setup_item()
        self.judge = 0 # judge the chat_board
        self.num_mes = 0
        self.mes_trigger = False

        self.finish = False
        self.cpt1_end = False
        self.next = 'cpt5'


        self.gray_tile = False
        self.yellow_tile = False
        self.stair = False
        self.judge = False
        self.speak = False
        self.barrier_kill = False
        self.chat_npc = 0
        self.num_mes = 0
        self.letter_judge = False
        self.mes_trigger = False
        self.satan_judge = False
        self.get_hoe = False
        self.door_judge = False
        self.get_satan_jewel = True
        self.chat_with_satan = True


        self.cpt4_map = load_js.load_map('./states/chapter4.json')  # [{"x": 293, "y": 379, "width": 211, "height": 43}]
        tools.trans_pixis(self.cpt4_map, default.CPT1_PIXIS_X, default.CPT1_PIXIS_Y)
        self.setup_goods()
        self.chat_npc = 0
        #self.setup_npc()





    def Cpt1_background(self):
        '''
        set up the background of the chapter_1
        :return:
        '''
        self.image = pygame.image.load('./data/map/chapter_4.png')
        self.image = pygame.transform.scale(self.image,(default.SCREEN_WIDTH,default.SCREEN_HEIGHT))

        pass
    def setup_goods(self):
        '''
        set up all the group of sprite
        :return:
        '''
        self.cpt4_group = pygame.sprite.Group()
        for item in self.cpt4_map :
            self.cpt4_group.add(goods.Goods(item['x'],item['y'],item['width'],item['height']))
        #print(self.cpt4_group)


    def setup_npc(self):
        self.chat_npc_list = []
        self.chat_npc_list.append(items_interation.Item("gray_tile"))
        self.chat_npc_list.append(items_interation.Item("yellow_tile"))
        self.chat_npc_list.append(items_interation.Item("stair"))
        self.chat_npc_list.append(items_interation.Item("jewel"))
        self.chat_npc_list.append((items_interation.Item("Bard-Shu Rui")))
        self.chat_npc_list.append(items_interation.Item("hoe"))
        self.chat_npc_list.append(items_interation.Item("axe"))
        self.chat_npc_list.append(items_interation.Item("Satan1"))
        self.chat_npc_list.append(items_interation.Item("Satan2"))
        self.chat_npc_list.append(items_interation.Item("door1"))
        self.chat_npc_list.append(items_interation.Item("door2"))
        self.chat = chat_board.Chat()




    def setup_role(self):
        '''
        set up the hero in the chapter_1
        :return:
        '''
        self.role = roles.Role(default.HUMAN_PICTURE[2])
        self.role.rect.x = 537
        self.role.rect.y = 568

    def setup_item(self):
        self.item_group = pygame.sprite.Group()
        self.barrier_group = pygame.sprite.Group()
        self.hoe_group = pygame.sprite.Group()
        self.jewel1 = goods.item_gooods(780,385,default.CPT4_ITEM[0])
        self.jewel2 = goods.item_gooods(108,205,default.CPT4_ITEM[0])
        self.jewel3 = goods.item_gooods(1008,327,default.CPT4_ITEM[0])
        self.hoe = goods.item_gooods(640,537, default.CPT4_ITEM[1])
        self.barrier1 = goods.item_gooods(947,121,default.CPT4_ITEM[2])
        self.barrier2 = goods.item_gooods(675,450,default.CPT4_ITEM[2])
        self.barrier3 = goods.item_gooods(106,240,default.CPT4_ITEM[2])

        self.item_group.add(self.jewel1)
        self.item_group.add(self.jewel2)
        self.item_group.add(self.jewel3)

        self.barrier_group.add(self.barrier1)
        self.barrier_group.add(self.barrier2)
        self.barrier_group.add(self.barrier3)

        self.hoe_group.add(self.hoe)


    def find_talk(self,keys):
        if (self.role.rect.x > 429 and self.role.rect.x <442) and (self.role.rect.y>523 and self.role.rect.y < 538): # gray_tile
            if keys[pygame.K_a]:
                self.judge = True
                self.gray_tile = True
                self.role.rect.x = 810
                self.role.rect.y = 259

        if (self.role.rect.x > 796 and self.role.rect.x <828) and (self.role.rect.y>280 and self.role.rect.y < 300): #gray_tile
            if keys[pygame.K_a]:
                self.judge = True
                self.gray_tile = True
                self.role.rect.x = 399
                self.role.rect.y = 535

        if (self.role.rect.x > 32 and self.role.rect.x <54) and (self.role.rect.y>427 and self.role.rect.y < 450): # stair
            if keys[pygame.K_a]:
                self.judge = True
                self.stair = True
                self.role.rect.x = 879
                self.role.rect.y = 442

        if (self.role.rect.x > 834 and self.role.rect.x <855) and (self.role.rect.y>427 and self.role.rect.y < 450): # stair2
            if keys[pygame.K_a]:
                self.judge = True
                self.stair = True
                self.role.rect.x = 69
                self.role.rect.y = 442
        if (self.role.rect.x > 32 and self.role.rect.x <50) and (self.role.rect.y>151 and self.role.rect.y < 190): # yellow_tile
            if keys[pygame.K_a]:
                self.judge = True
                self.yellow_tile = True
                self.role.rect.x = 675
                self.role.rect.y = 85

        if (self.role.rect.x > 663 and self.role.rect.x <690) and (self.role.rect.y>97 and self.role.rect.y < 127): # yellow_tile
            if keys[pygame.K_a]:
                self.judge = True
                self.yellow_tile = True
                self.role.rect.x = 33
                self.role.rect.y = 211

        if (self.role.rect.x > 30 and self.role.rect.x <52) and (self.role.rect.y>520 and self.role.rect.y < 538): # letter
            if keys[pygame.K_a]:
                self.judge = True
                self.letter_judge = True

        if (self.role.rect.x > 798 and self.role.rect.x <825) and (self.role.rect.y>230 and self.role.rect.y < 243): # satan
            if keys[pygame.K_a]:
                if self.chat_with_satan:
                    self.judge = True
                    self.satan_judge = True

        if (self.role.rect.x > 533 and self.role.rect.x < 555) and (self.role.rect.y > 73 and self.role.rect.y < 89):
            if keys[pygame.K_a]:
                self.judge = True
                self.door_judge = True

        self.jewel_collision = pygame.sprite.spritecollideany(self.role, self.item_group)  # jewel
        if self.jewel_collision:
            if keys[pygame.K_a]:
                self.judge = True
                self.speak = True
                self.chat_npc = self.chat_npc_list[3]
                default.HERO_ITEM["jewel"] = default.HERO_ITEM["jewel"] + 1
                self.jewel_collision.kill()

        self.hoe_collision = pygame.sprite.spritecollideany(self.role, self.hoe_group)
        if self.hoe_collision :
            if keys[pygame.K_a]:
                self.judge = True
                self.speak = True
                self.chat_npc = self.chat_npc_list[5]
                self.get_hoe = True
                self.hoe_collision.kill()



    def draw_items(self, judge, surface, keys):
        if judge:
            if self.gray_tile:
                self.gray_tile = False
                self.speak = True
                self.chat_npc = self.chat_npc_list[0]

            if self.yellow_tile:
                self.yellow_tile = False
                self.speak = True
                self.chat_npc = self.chat_npc_list[1]

            if self.stair:
                self.stair = False
                self.speak = True
                self.chat_npc = self.chat_npc_list[2]

            if self.letter_judge:
                surface.blit(default.ITEM_LIST[2], (100, 75))
                if keys[pygame.K_SPACE]:
                    self.letter_judge = False
                    self.speak = True
                    self.chat_npc = self.chat_npc_list[4]

            if self.satan_judge:
                self.satan_judge = False
                self.speak = True
                self.chat_with_satan = False
                if default.HERO_ITEM["pearls"] == 1 and default.HERO_ITEM["sword"] == 1 :
                    if self.get_satan_jewel:
                        self.get_satan_jewel = False
                        default.HERO_ITEM["jewel"] = default.HERO_ITEM["jewel"] + 1
                    self.chat_npc = self.chat_npc_list[8]


                else :

                    self.chat_npc = self.chat_npc_list[7]

            if self.door_judge :
                self.door_judge = False
                self.speak = True
                if default.HERO_ITEM["jewel"] == 4 :
                    self.chat_npc = self.chat_npc_list[10]
                else:
                    self.chat_npc = self.chat_npc_list[9]


            if self.speak:
                for key, value in self.chat_npc.chat_mes[self.num_mes].items():
                    # 670
                    if key == 'Warrior':
                        default.CHAT_START_Y = 670
                    self.chat.print_mes(self.chat_npc.chat_mes[self.num_mes][key], surface)
                    default.CHAT_START_Y = 570
                if self.chat_npc.attri == "npc":
                    surface.blit(self.chat_npc.npc_pit, (default.HUMAN_PICT_WIDTH, default.HUMAN_PICT_HEIGHT))  # npc
                surface.blit(self.role.hero_pit, (default.HERO_PICT_WIDTH, default.HERO_PICT_HEIGHT))  # hero
                # print(len(self.chat_npc.chat_mes))

                if len(self.chat_npc.chat_mes) == (self.num_mes + 1):
                    # print(self.chat_npc.name)
                    if  default.HERO_ITEM["jewel"] == 4:
                        if (self.role.rect.x > 533 and self.role.rect.x < 555) and (self.role.rect.y > 73 and self.role.rect.y < 89):
                            self.num_mes = 0
                            self.judge = False
                            self.mes_trigger = False
                            self.speak = False
                            self.finish = True
                            return

                    if self.chat_npc == self.chat_npc_list[7] :
                        self.num_mes = 0
                        self.judge = False
                        self.mes_trigger = False
                        self.speak = False
                        self.next = 'gameover'
                        self.finish = True
                        return


                    if keys[pygame.K_SPACE]:
                        self.num_mes = 0
                        self.judge = False
                        self.speak = False
                        self.mes_trigger = False
                        return

                if len(self.chat_npc.chat_mes) > (self.num_mes):
                    if keys[pygame.K_SPACE]:
                        self.mes_trigger = True
                    if keys[pygame.K_SPACE] == False and self.mes_trigger == True:
                        self.num_mes += 1
                        self.mes_trigger = False























    def update_position(self):

        self.role.rect.x += self.role.x_vel
        self.x_collide()
        self.x_barrier_collid()
        self.role.rect.y += self.role.y_vel

        self.y_collide()
        self.y_barrier_collide()
        #self.jewel_collide()
        if (self.role.rect.x>501 and self.role.rect.x<580) and self.role.rect.y> 660 :
            self.finish = True
        #print(self.role.rect)

   # def jewel_collide(self,keys):



    def x_collide(self):
        '''
        judge whether there is  collision in the x_axis. if yes, do something
        :return:
        '''
        self.goods_collision = pygame.sprite.spritecollideany(self.role,self.cpt4_group)

        if self.goods_collision :
            if self.role.rect.x < self.goods_collision.rect.x :
                self.role.rect.right = self.goods_collision.rect.left
            else :
                self.role.rect.left = self.goods_collision.rect.right
            self.role.x_vel = 0

    def x_barrier_collid(self):
        self.goods_collision = pygame.sprite.spritecollideany(self.role,self.barrier_group)

        if self.goods_collision :
            # if self.barrier_kill:
            if self.get_hoe:
                self.goods_collision.kill()
            else:
                self.speak = True
                self.judge = True
                self.chat_npc = self.chat_npc_list[6]
                if self.role.rect.x < self.goods_collision.rect.x :
                    self.role.rect.right = self.goods_collision.rect.left
                else :
                    self.role.rect.left = self.goods_collision.rect.right
                self.role.x_vel = 0
        pass



    def y_collide(self):
        '''
        judge whether there is  collision in the x_axis. if yes, do something
        :return:
        '''
        self.goods_collision = pygame.sprite.spritecollideany(self.role, self.cpt4_group)
        if self.goods_collision:
            if self.role.rect.bottom < self.goods_collision.rect.bottom:
                self.role.rect.bottom = self.goods_collision.rect.top
            else:
                self.role.rect.top = self.goods_collision.rect.bottom
            self.role.y_vel = 0


    def y_barrier_collide(self):
        self.goods_collision = pygame.sprite.spritecollideany(self.role, self.barrier_group)
        if self.goods_collision:
            if self.get_hoe:
                self.goods_collision.kill()
            else:
                self.speak = True
                self.judge = True
                self.chat_npc = self.chat_npc_list[6]
                if self.role.rect.bottom < self.goods_collision.rect.bottom:
                    self.role.rect.bottom = self.goods_collision.rect.top
                else:
                    self.role.rect.top = self.goods_collision.rect.bottom
                self.role.y_vel = 0
        pass

    def update(self,surface,keys):
        if self.judge != 1:
            self.role.update(keys)
        self.update_position()
        self.find_talk(keys)
        self.draw(surface,keys)



    def draw(self,surface,keys):
        print(default.HERO_ITEM["jewel"])
        surface.blit(self.image,(0,0))
        self.item_group.draw(surface)
        self.barrier_group.draw(surface)
        self.hoe_group.draw(surface)
        surface.blit(self.role.role_image,self.role.rect)
        self.draw_items(self.judge,surface,keys)


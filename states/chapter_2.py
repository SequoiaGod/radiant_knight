import pygame
from sources import default,tools,setup
from states import roles,goods,load_js,npc,chat_board,items_interation


class Cpt2 :
    def __init__(self):
        self.state_name = 'cpt2'
        self.set_music = True
        self.finish = False
        self.cpt2_end = False
        self.next = 'cpt3'
        self.cpt2_background()
        self.setup_role()
        self.setup_npc()

        self.chat_sound = pygame.mixer.Sound('./data/sounds/chat.mp3')
        self.judge = False
        self.mage_judge = False
        self.num_mes = 0
        self.mes_trigger = False
        self.stone_judge = False
        self.letter_judge = False
        self.monument_judge = False
        self.teleportation_judge = False
        self.code = False
        self.teleportation = False
        self.speak = False # if the speak is TRUE, that means the npc need to speak something
        self.end = False
        self.chat_npc = 0

        self.cpt2_map = load_js.load_map('./states/chapter2.json')  # [{"x": 293, "y": 379, "width": 211, "height": 43}]
        tools.trans_pixis(self.cpt2_map, default.CPT2_PIXIS_X, default.CPT2_PIXIS_Y)
        self.setup_goods()
        self.setup_item()

    def cpt2_background(self):
        self.image = pygame.image.load('./data/map/chapter_2.png')
        self.image = pygame.transform.scale(self.image, (default.SCREEN_WIDTH, default.SCREEN_HEIGHT))

    def setup_goods(self):
        '''
        set up all the group of sprite
        :return:
        '''
        self.cpt2_group = pygame.sprite.Group()
        for item in self.cpt2_map :
            self.cpt2_group.add(goods.Goods(item['x'],item['y'],item['width'],item['height']))
        print(self.cpt2_group)

    def setup_npc(self):
        '''
        init the npc who I need in this chapter
        :return:
        '''
        self.mage = npc.NPC("Bard-Yan Jun",default.info[2],default.HUMAN_PICTURE[3])
        self.chat = chat_board.Chat()
        self.chat_npc_list = [self.mage]
        self.monument1 = items_interation.Item("monument1")
        self.monument2 = items_interation.Item("monument2")
        self.Letter2 = items_interation.Item("Letter2")
        self.Slate2 = items_interation.Item("Slate2")
        self.chat_npc_list.append(self.monument1)
        self.chat_npc_list.append(self.monument2)
        self.chat_npc_list.append(self.Letter2)
        self.chat_npc_list.append(self.Slate2)
        self.chat_npc_list.append(items_interation.Item("teleportation1"))
        self.chat_npc_list.append(items_interation.Item("teleportation2"))
        self.mage.rect.x = 70
        self.mage.rect.y = 354

    def setup_item(self):
        pass
    def setup_role(self):
        '''
        set up the hero in the chapter_2
        :return:
        '''
        self.role = roles.Role(default.HUMAN_PICTURE[2])
        self.role.current_structure = self.role.stop_structure
        self.role.rect.x = 513
        self.role.rect.y = 624

    def find_talk(self, keys):
        if (self.role.rect.x > 166 and self.role.rect.x <205) and (self.role.rect.y>340 and self.role.rect.y < 370): # mage
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.mage_judge = True
        if (self.role.rect.x > 228 and self.role.rect.x < 260) and (self.role.rect.y > 100 and self.role.rect.y < 120): # slate site
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.stone_judge = True
                default.HERO_ITEM["pearls"] = 1
        if (self.role.rect.x >550  and self.role.rect.x < 575) and (self.role.rect.y > 516 and self.role.rect.y < 538): # letter
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.letter_judge = True
        if (self.role.rect.x >798  and self.role.rect.x < 827) and (self.role.rect.y > 339 and self.role.rect.y < 360):# monument site
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.monument_judge = True

        if (self.role.rect.x >880  and self.role.rect.x < 941) and (self.role.rect.y > 134 and self.role.rect.y < 216):# teleprotatio n site
            if keys[pygame.K_a]:
                #self.judge = True
                self.judge = True
                default.chat_sound_start = True
                self.teleportation_judge = True

        pass

    def draw_items(self,judge,surface,keys):

        if judge :

            if self.mage_judge:
                self.mage_judge = False
                self.chat_npc=self.chat_npc_list[0]
                self.code = True
                self.speak = True
            if self.monument_judge:
                self.monument_judge =False
                if self.code:
                    self.speak = True

                    self.chat_npc = self.chat_npc_list[2]
                    self.teleportation = True
                else:
                    self.speak = True
                    self.chat_npc = self.chat_npc_list[1]

            if self.teleportation_judge:
                self.teleportation_judge = False
                if self.teleportation:
                    self.speak = True

                    self.chat_npc = self.chat_npc_list[6]

                else:
                    self.speak = True

                    self.chat_npc = self.chat_npc_list[5]
            if self.speak:
                for key,value in self.chat_npc.chat_mes[self.num_mes].items():
                    #670
                    if key == 'Warrior':
                        default.CHAT_START_Y = 670
                    self.chat.print_mes(self.chat_npc.chat_mes[self.num_mes][key],surface)
                    default.CHAT_START_Y = 570
                if self.chat_npc.attri == "npc":
                    surface.blit(self.chat_npc.npc_pit,(default.HUMAN_PICT_WIDTH,default.HUMAN_PICT_HEIGHT)) # npc
                surface.blit(self.role.hero_pit,(default.HERO_PICT_WIDTH,default.HERO_PICT_HEIGHT)) #hero
                #print(len(self.chat_npc.chat_mes))


                if len(self.chat_npc.chat_mes) == (self.num_mes + 1):
                    self.chat_sound_start = True
                    #print(self.chat_npc.name)
                    if self.teleportation:
                        if (self.role.rect.x > 880 and self.role.rect.x < 941) and (self.role.rect.y > 134 and self.role.rect.y < 216):
                            if keys[pygame.K_SPACE] :
                                self.num_mes = 0
                                self.judge = False
                                self.mes_trigger = False
                                self.mage_judge = False
                                self.speak = False
                                self.finish = True
                                return
                    if keys[pygame.K_SPACE] :
                        self.num_mes = 0
                        self.chat_sound_start = True
                        self.judge = False
                        self.mes_trigger = False
                        self.mage_judge = False
                        self.speak = False
                        return
                if len(self.chat_npc.chat_mes) > (self.num_mes):
                    if keys[pygame.K_SPACE]:
                        self.mes_trigger = True
                    if keys[pygame.K_SPACE] == False and self.mes_trigger == True:
                        self.num_mes += 1
                        self.mes_trigger = False


            if self.stone_judge:
                surface.blit(default.ITEM_LIST[1], (100, 75))
                default.HERO_ITEM["pearls"] = 1
                if keys[pygame.K_SPACE]:
                    self.stone_judge = False

                    self.chat_npc = self.chat_npc_list[4]
                    self.speak = True
                    self.chat_npc = self.chat_npc_list[4]

            if self.letter_judge:
                surface.blit(default.ITEM_LIST[0],(100,75))
                if keys[pygame.K_SPACE]:
                    self.letter_judge = False

                    self.speak = True
                    self.chat_npc = self.chat_npc_list[3]





    def update_position(self):

        self.role.rect.x += self.role.x_vel
        self.x_collide()
        self.role.rect.y += self.role.y_vel

        self.y_collide()
        # y=730
        # if (self.role.rect.x>500 and self.role.rect.x<540) and self.role.rect.y> 660 :
        #     self.finish = True
        print(self.role.rect)

    def x_collide(self):
        '''
        judge whether there is  collision in the x_axis. if yes, do something
        :return:
        '''
        self.goods_collision = pygame.sprite.spritecollideany(self.role, self.cpt2_group)

        if self.goods_collision:
            if self.role.rect.x < self.goods_collision.rect.x:
                self.role.rect.right = self.goods_collision.rect.left
            else:
                self.role.rect.left = self.goods_collision.rect.right
            self.role.x_vel = 0

    def y_collide(self):
        '''
        judge whether there is  collision in the x_axis. if yes, do somethi
        :return:
        '''
        self.goods_collision = pygame.sprite.spritecollideany(self.role, self.cpt2_group)
        if self.goods_collision:
            if self.role.rect.bottom < self.goods_collision.rect.bottom:
                self.role.rect.bottom = self.goods_collision.rect.top
            else:
                self.role.rect.top = self.goods_collision.rect.bottom
            self.role.y_vel = 0
    def update(self,surface,keys):
        '''
        update all of parameter in this chapter
        :param surface:
        :param keys:
        :return:
        '''
        if self.judge != 1:
            self.role.update(keys)
        tools.play_chatsound(default.chat_sound_start,self.chat_sound)
        self.find_talk(keys)
        self.update_position()
        self.mage.update()
        if self.set_music:
            self.set_music = False
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load('./data/sounds/234.mp3')
            pygame.mixer.music.play(-1)
        self.draw(surface,keys)



    def draw(self,surface,keys):
        surface.blit(self.image,(0,0))
        surface.blit(self.mage.role_image,self.mage.rect)
        surface.blit(self.role.role_image,self.role.rect)
        self.draw_items(self.judge,surface,keys)
        pass
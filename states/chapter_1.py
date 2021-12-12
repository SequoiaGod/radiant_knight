import pygame
from sources import default,tools,setup
from states import roles,goods,load_js,npc,chat_board

class Cpt1:
    '''
        this is chapter one code
    '''
    def __init__(self):
        self.state_name = 'cpt1'
        self.Cpt1_background()
        self.setup_role()
        self.judge = 0 # judge the chat_board
        self.num_mes = 0
        self.mes_trigger = False
        self.set_music = True

        self.finish = False
        self.cpt1_end = False
        self.next = 'cpt2'
        self.cpt1_map = load_js.load_map('./states/chapter1.json')  # [{"x": 293, "y": 379, "width": 211, "height": 43}]
        tools.trans_pixis(self.cpt1_map, default.CPT1_PIXIS_X, default.CPT1_PIXIS_Y)
        self.setup_goods()
        self.chat_npc = 0
        self.setup_npc()
        # pygame.mixer.music.load('./data/sounds/cpt1.mp3')
        # pygame.mixer.music.play(1,100)




    def Cpt1_background(self):
        '''
        set up the background of the chapter_1
        :return:
        '''
        self.image = pygame.image.load('./data/map/chapter_1.png')
        self.image = pygame.transform.scale(self.image,(default.SCREEN_WIDTH,default.SCREEN_HEIGHT))

        pass
    def setup_goods(self):
        '''
        set up all the group of sprite
        :return:
        '''
        self.cpt1_group = pygame.sprite.Group()
        for item in self.cpt1_map :
            self.cpt1_group.add(goods.Goods(item['x'],item['y'],item['width'],item['height']))
        #print(self.cpt1_group)

    def setup_npc(self):
        '''
        set up all the npc in the chapter_1
        :return:
        '''
        self.soldier1 = npc.NPC("soldier1",default.info[0],default.HUMAN_PICTURE[0])
        self.soldier2 = npc.NPC("soldier2",default.info[0],default.HUMAN_PICTURE[0])
        self.prince = npc.NPC("prince",default.info[1],default.HUMAN_PICTURE[1])
        self.npc_list = [self.soldier1,self.soldier2,self.prince]
        self.chat = chat_board.Chat()
        self.soldier1.rect.x = 377
        self.soldier1.rect.y = 376

        self.soldier2.rect.x = 634
        self.soldier2.rect.y = 376

        self.prince.rect.x = 505
        self.prince.rect.y = 320




    def setup_role(self):
        '''
        set up the hero in the chapter_1
        :return:
        '''
        self.role = roles.Role(default.HUMAN_PICTURE[2])
        self.role.rect.x = 504
        self.role.rect.y = 649

    def Cpt1_play(self):

        pass




    def find_talk(self,keys):
        for npc in self.npc_list :
            self.npc_collision = pygame.sprite.collide_rect(self.role,npc)
            if self.npc_collision :
                if keys[pygame.K_a] :

                    self.judge = 1


                    self.chat_npc = npc




    def draw_chat_board(self,judge,surface,keys):

        if judge :
            for key,value in self.chat_npc.chat_mes[self.num_mes].items():
                #670
                if key == 'Warrior':
                    default.CHAT_START_Y = 670
                self.chat.print_mes(self.chat_npc.chat_mes[self.num_mes][key],surface)
                default.CHAT_START_Y = 570
            surface.blit(self.chat_npc.npc_pit,(default.HUMAN_PICT_WIDTH,default.HUMAN_PICT_HEIGHT)) # npc
            surface.blit(self.role.hero_pit,(default.HERO_PICT_WIDTH,default.HERO_PICT_HEIGHT)) #hero
            #print(len(self.chat_npc.chat_mes))


            if len(self.chat_npc.chat_mes) == (self.num_mes + 1):
                #print(self.chat_npc.name)
                if self.chat_npc.name =="prince" :
                    self.cpt1_end = True
                if keys[pygame.K_SPACE] :
                    self.num_mes = 0
                    self.judge = 0
                    self.mes_trigger = False
                    return

            if len(self.chat_npc.chat_mes) > (self.num_mes):
                if keys[pygame.K_SPACE]:
                    self.mes_trigger = True
                if keys[pygame.K_SPACE] == False and self.mes_trigger == True :

                    self.num_mes += 1
                    self.mes_trigger = False








    def update_position(self):

        self.role.rect.x += self.role.x_vel
        self.x_collide()
        self.role.rect.y += self.role.y_vel

        self.y_collide()
        if (self.role.rect.x>500 and self.role.rect.x<540) and self.role.rect.y> 660 : # new chapter judgement
            if self.cpt1_end :
                self.finish = True
        print(self.role.rect)

    def x_collide(self):
        '''
        judge whether there is  collision in the x_axis. if yes, do something
        :return:
        '''
        self.goods_collision = pygame.sprite.spritecollideany(self.role,self.cpt1_group)

        if self.goods_collision :
            if self.role.rect.x < self.goods_collision.rect.x :
                self.role.rect.right = self.goods_collision.rect.left
            else :
                self.role.rect.left = self.goods_collision.rect.right
            self.role.x_vel = 0


    def y_collide(self):
        '''
        judge whether there is  collision in the x_axis. if yes, do somethi
        :return:
        '''
        self.goods_collision = pygame.sprite.spritecollideany(self.role, self.cpt1_group)
        if self.goods_collision:
            if self.role.rect.bottom < self.goods_collision.rect.bottom:
                self.role.rect.bottom = self.goods_collision.rect.top
            else:
                self.role.rect.top = self.goods_collision.rect.bottom
            self.role.y_vel = 0

    def update(self, surface,keys):
        #print(keys[pygame.K_SPACE])
        '''
        update all the element which is changed
        :param surface: the main window
        :param keys: from keyboard or mouse
        :return:
        '''
        if self.judge != 1:
            self.role.update(keys)
        self.find_talk(keys)
        self.update_position()



        self.soldier1.update()
        self.soldier2.update()
        self.prince.update()
        if self.set_music:
            self.set_music = False
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load('./data/sounds/cpt1.mp3')
            pygame.mixer.music.play(-1)
        self.draw(surface,keys)

    def draw(self,surface,keys):
        surface.blit(self.image, (0, 0))
        surface.blit(self.soldier1.role_image,self.soldier1.rect)
        surface.blit(self.soldier2.role_image,self.soldier2.rect)
        surface.blit(self.prince.role_image,self.prince.rect)




        surface.blit(self.role.role_image,self.role.rect)
        self.draw_chat_board(self.judge,surface,keys)



import pygame
from sources import default,tools,setup
from states import roles,goods,load_js,npc,chat_board

class Cpt5:
    '''
        this is chapter one code
    '''
    def __init__(self):
        self.state_name = 'cpt5'
        self.Cpt1_background()
        self.setup_role()
        self.setup_npc()


        self.judge = 0 # judge the chat_board
        self.num_mes = 0
        self.mes_trigger = False

        self.finish = False
        self.cpt1_end = False
        self.next = 'cpt6'
        self.chat_sound = pygame.mixer.Sound('./data/sounds/chat.mp3')
        self.chat_sound_start = True
        self.cpt5_map = load_js.load_map('./states/chapter5.json')  # [{"x": 293, "y": 379, "width": 211, "height": 43}]
        tools.trans_pixis(self.cpt5_map, default.CPT1_PIXIS_X, default.CPT1_PIXIS_Y)
        self.setup_goods()
        self.chat_npc = 0
        #self.setup_npc()





    def Cpt1_background(self):
        '''
        set up the background of the chapter_1
        :return:
        '''
        self.image = pygame.image.load('./data/map/chapter_5.png')
        self.image = pygame.transform.scale(self.image,(default.SCREEN_WIDTH,default.SCREEN_HEIGHT))

        pass
    def setup_goods(self):
        '''
        set up all the group of sprite
        :return:
        '''
        self.cpt5_group = pygame.sprite.Group()
        for item in self.cpt5_map :
            self.cpt5_group.add(goods.Goods(item['x'],item['y'],item['width'],item['height']))
        #print(self.cpt5_group)

    def setup_npc(self):
        self.king = npc.NPC("King",default.info[3],default.HUMAN_PICTURE[4])
        self.chat = chat_board.Chat()
        self.npc_list = [self.king]
        self.king.rect.x = 507
        self.king.rect.y = 299




    def setup_role(self):
        '''
        set up the hero in the chapter_1
        :return:
        '''
        self.role = roles.Role(default.HUMAN_PICTURE[2])
        self.role.rect.x = 507
        self.role.rect.y = 665


    def find_talk(self,keys):
        for npc in self.npc_list :
            self.npc_collision = pygame.sprite.collide_rect(self.role,npc)
            if self.npc_collision :
                if keys[pygame.K_a] :

                    self.judge = 1


                    self.chat_npc = npc






    def draw_chat_board(self,judge,surface,keys):

        if judge :
            if self.chat_sound_start :
                #self.chat_sound.play(1)
                self.chat_sound_start = False
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
                self.chat_sound_start = True
                #print(self.chat_npc.name)
                if self.chat_npc.name == "King":
                    self.finish = True
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
        if (self.role.rect.x>500 and self.role.rect.x<540) and self.role.rect.y> 660 :
            if self.cpt1_end :
                self.finish = True
        print(self.role.rect)

    def x_collide(self):
        '''
        judge whether there is  collision in the x_axis. if yes, do something
        :return:
        '''
        self.goods_collision = pygame.sprite.spritecollideany(self.role,self.cpt5_group)

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
        self.goods_collision = pygame.sprite.spritecollideany(self.role, self.cpt5_group)
        if self.goods_collision:
            if self.role.rect.bottom < self.goods_collision.rect.bottom:
                self.role.rect.bottom = self.goods_collision.rect.top
            else:
                self.role.rect.top = self.goods_collision.rect.bottom
            self.role.y_vel = 0

    def update(self,surface,keys):
        if self.judge != 1:
            self.role.update(keys)
        self.find_talk(keys)
        self.update_position()


        self.king.update()
        self.draw(surface,keys)



    def draw(self,surface,keys):
        surface.blit(self.image,(0,0))
        surface.blit(self.king.role_image,self.king.rect)
        surface.blit(self.role.role_image,self.role.rect)
        self.draw_chat_board(self.judge, surface, keys)

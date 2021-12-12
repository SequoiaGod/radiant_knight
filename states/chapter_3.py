import pygame
from sources import default,tools,setup
from states import roles,goods,load_js,npc,chat_board,items_interation




class Cpt3 :
    def __init__(self):
        self.state_name = 'cpt3'
        self.finish = False
        self.next = 'cpt4'
        self.cpt3_background()
        self.setup_role()
        self.setup_npc()

        self.judge = False
        self.num_mes = 0
        self.mes_trigger = False
        self.mage_judge = False
        self.code2 = False
        self.letter_judge = False
        self.rope_judge = False
        self.monument_judge = False
        self.sword_judge = False
        self.sword =False
        self.teleport_judge = False
        self.teleport = False
        self.speak = False
        self.end = False
        self.chat_npc = 0
        self.chat_sound = pygame.mixer.Sound('./data/sounds/chat.mp3')


        self.cpt3_map = load_js.load_map('./states/chapter3.json')  # [{"x": 293, "y": 379, "width": 211, "height": 43}]
        tools.trans_pixis(self.cpt3_map, default.CPT1_PIXIS_X, default.CPT1_PIXIS_Y)
        self.setup_goods()
        self.setup_item()

    def setup_goods(self):
        '''
        set up all the group of sprite
        :return:
        '''
        self.cpt3_group = pygame.sprite.Group()
        for item in self.cpt3_map :
            self.cpt3_group.add(goods.Goods(item['x'],item['y'],item['width'],item['height']))
        print(self.cpt3_group)

    def cpt3_background(self):
        self.image = pygame.image.load('./data/map/chapter_3.png')
        self.image = pygame.transform.scale(self.image, (default.SCREEN_WIDTH, default.SCREEN_HEIGHT))


    def setup_role(self):
        '''
        set up the hero in the chapter_1
        :return:
        '''
        self.role = roles.Role(default.HUMAN_PICTURE[2])
        self.role.current_structure = self.role.stop_structure
        self.role.rect.x = 539
        self.role.rect.y = 569

    def setup_npc(self):
        self.mage = npc.NPC("Bard——Yang Yu",default.info[4],default.HUMAN_PICTURE[3])
        self.chat = chat_board.Chat()
        self.mage.rect.x = 985
        self.mage.rect.y = 435
        self.sword_img = pygame.image.load('./data/item/sword.png')

        self.chat_npc_list = [self.mage]
        self.chat_npc_list.append(items_interation.Item('monument1'))
        self.chat_npc_list.append(items_interation.Item('monument2'))
        self.chat_npc_list.append(items_interation.Item('Letter3'))
        self.chat_npc_list.append(items_interation.Item('row'))
        self.chat_npc_list.append(items_interation.Item('statue'))
        self.chat_npc_list.append(items_interation.Item('teleportation1'))
        self.chat_npc_list.append(items_interation.Item('teleportation2'))
        #[ 0mage , 1monument1 , 2monument2 , 3letter , 4rope , 5sword , 6teleport1 , 7teleport2]

    def setup_item(self):
        pass

    def find_talk(self,keys):
        # mage judge
        if(self.role.rect.x > 900 and self.role.rect.x <918) and (self.role.rect.y > 420 and self.role.rect.y < 447):
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.mage_judge = True
        # rope judge
        if (self.role.rect.x > 525 and self.role.rect.x < 555) and (self.role.rect.y > 122 and self.role.rect.y < 137):
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.rope_judge =True
        #sword judge
        if (self.role.rect.x > 130 and self.role.rect.x < 160) and (self.role.rect.y > 148 and self.role.rect.y < 180):
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.sword_judge = True
        #letter judge
        if (self.role.rect.x > 575 and self.role.rect.x < 600) and (self.role.rect.y > 537 and self.role.rect.y < 570):
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.letter_judge =True
        #monument judge
        if (self.role.rect.x > 655 and self.role.rect.x < 700) and (self.role.rect.y > 368 and self.role.rect.y < 381):
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.monument_judge =True
        #teleport judge
        if (self.role.rect.x > 813 and self.role.rect.x < 875) and (self.role.rect.y > 135 and self.role.rect.y < 221):
            if keys[pygame.K_a]:
                self.judge = True
                default.chat_sound_start = True
                self.teleport_judge = True

    def draw_items(self,judge,surface,keys):
        if self.sword:
            if default.HERO_ITEM['sword'] != 1:
                surface.blit(self.sword_img, (129, 135))
        else:
            pass
        if judge:
            if self.chat_sound_start :
                #self.chat_sound.play(1)
                self.chat_sound_start = False
            #mage
            if self.mage_judge:
                self.mage_judge = False
                self.chat_npc = self.chat_npc_list[0]
                self.code2 = True
                self.speak = True
            #monument
            if self.monument_judge:
                self.monument_judge = False
                if self.code2 == False:
                    self.chat_npc = self.chat_npc_list[1]
                    self.speak = True
                else:
                    self.chat_npc = self.chat_npc_list[2]
                    self.speak = True
                    self.teleport = True
            #letter
            if self.letter_judge:
                surface.blit(default.ITEM_LIST[3], (100, 75))
                if keys[pygame.K_SPACE]:
                    self.letter_judge = False
                    self.chat_npc = self.chat_npc_list[3]
                    self.speak = True
            #rope
            if self.rope_judge:
                self.rope_judge = False
                self.chat_npc =self.chat_npc_list[4]
                self.speak = True
                self.sword = True
            #sword
            if self.sword_judge:
                self.sword_judge =False
                default.HERO_ITEM["sword"] = 1
                self.chat_npc = self.chat_npc_list[5]
                self.speak = True
                self.sword = False
            #teleport
            if self.teleport_judge:
                self.teleport_judge = False
                if self.teleport == False:
                    self.chat_npc = self.chat_npc_list[6]
                    self.speak = True
                else :
                    self.chat_npc = self.chat_npc_list[7]
                    self.speak = True
            # [ 0mage , 1monument1 , 2monument2 , 3letter , 4rope , 5sword , 6teleport1 , 7teleport2]
            if self.speak:
                for key,value in self.chat_npc.chat_mes[self.num_mes].items():
                    if key == 'Warrior':
                        default.CHAT_START_Y = 670
                    self.chat.print_mes(self.chat_npc.chat_mes[self.num_mes][key],surface)
                    default.CHAT_START_Y = 570
                if self.chat_npc.attri == 'npc':
                    surface.blit(self.chat_npc.npc_pit,(default.HUMAN_PICT_WIDTH,default.HUMAN_PICT_HEIGHT))
                surface.blit(self.role.hero_pit,(default.HERO_PICT_WIDTH,default.HERO_PICT_HEIGHT))

                if len(self.chat_npc.chat_mes) == (self.num_mes +1):
                    self.chat_sound_start = True
                    if self.teleport:
                        if(self.role.rect.x > 813 and self.role.rect.x < 875) and (self.role.rect.y > 135 and self.role.rect.y < 221):
                            if keys[pygame.K_SPACE]:
                                self.num_mes = 0
                                self.judge = False
                                self.mes_trigger = False
                                self.mage_judge = False
                                self.speak = False
                                self.finish = True
                                return
                    if keys[pygame.K_SPACE]:
                        self.num_mes = 0
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


    def update_position(self):

        self.role.rect.x += self.role.x_vel
        self.x_collide()
        self.role.rect.y += self.role.y_vel

        self.y_collide()
        # y=730

        if (self.role.rect.x>500 and self.role.rect.x<540) and self.role.rect.y> 660 : # new chapter judgement

            self.finish = True

        print(self.role.rect)

    def x_collide(self):
        '''
        judge whether there is  collision in the x_axis. if yes, do something
        :return:
        '''
        self.goods_collision = pygame.sprite.spritecollideany(self.role, self.cpt3_group)

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
        self.goods_collision = pygame.sprite.spritecollideany(self.role, self.cpt3_group)
        if self.goods_collision:
            if self.role.rect.bottom < self.goods_collision.rect.bottom:
                self.role.rect.bottom = self.goods_collision.rect.top
            else:
                self.role.rect.top = self.goods_collision.rect.bottom
            self.role.y_vel = 0

    def update(self,surface,keys):
        if self.judge != 1:
            self.role.update(keys)
        tools.play_chatsound(default.chat_sound_start,self.chat_sound)
        self.update_position()
        self.find_talk(keys)
        self.mage.update()
        self.draw(surface,keys)



    def draw(self,surface,keys):
        surface.blit(self.image,(0,0))
        surface.blit(self.role.role_image,self.role.rect)
        surface.blit(self.mage.role_image,self.mage.rect)
        self.draw_items(self.judge,surface,keys)
        pass
import pygame
from sources import default,tools,setup
from states import roles,goods,load_js,npc,chat_board

class Cpt1:
    '''
        this is chapter one code
    '''
    def __init__(self):
        self.Cpt1_background()
        self.setup_role()
        self.judge = 0
        self.finish = False
        self.next = 'cpt2'
        self.cpt1_map = load_js.load_map('./states/chapter1.json')  # [{"x": 293, "y": 379, "width": 211, "height": 43}]
        tools.trans_pixis(self.cpt1_map)
        self.setup_goods()

        self.setup_npc()
        pygame.mixer.music.load('./data/sounds/cpt1.mp3')
        pygame.mixer.music.play(1,100)




    def Cpt1_background(self):
        self.image = pygame.image.load('./data/map/chapter_1new.png')
        self.image = pygame.transform.scale(self.image,(default.SCREEN_WIDTH,default.SCREEN_HEIGHT))

        pass
    def setup_goods(self):
        self.cpt1_group = pygame.sprite.Group()
        for item in self.cpt1_map :
            self.cpt1_group.add(goods.Goods(item['x'],item['y'],item['width'],item['height']))
        print(self.cpt1_group)

    def setup_npc(self):
        self.soldier1 = npc.NPC("soldier1",default.info[0])
        self.soldier2 = npc.NPC("soldier2",default.info[0])
        self.prince = npc.NPC("prince",default.info[1])
        self.npc_list = [self.soldier1,self.soldier2,self.prince]
        self.chat = chat_board.Chat()
        self.soldier1.rect.x = 335
        self.soldier1.rect.y = 515

        self.soldier2.rect.x = 460
        self.soldier2.rect.y = 515

        self.prince.rect.x = 620
        self.prince.rect.y = 401

        self.chat.rect.x = 0
        self.chat.rect.y = 599


    def setup_role(self):
        self.role = roles.Role()
        self.role.rect.x = 390
        self.role.rect.y = 625

    def Cpt1_play(self):

        pass

    def update(self, surface,keys):
        self.role.update(keys)
        self.find_talk(keys)
        self.update_position()

        self.draw(surface)



    def find_talk(self,keys):
        for npc in self.npc_list :
            self.npc_collision = pygame.sprite.collide_rect(self.role,npc)
            if self.npc_collision :
                if keys[pygame.K_a] :
                    self.judge = 1
                    print(npc.name)

        pass

    def draw_chat_board(self,judge,surface):
        if judge :
            surface.blit(self.chat.img, self.chat.rect)
            surface.blit(self.chat.mes1, (50, 650))

    def update_position(self):

        self.role.rect.x += self.role.x_vel
        self.x_collide()
        self.role.rect.y += self.role.y_vel

        self.y_collide()
        # print(self.role.rect)

    def x_collide(self):
        self.goods_collision = pygame.sprite.spritecollideany(self.role,self.cpt1_group)

        if self.goods_collision :
            if self.role.rect.x < self.goods_collision.rect.x :
                self.role.rect.right = self.goods_collision.rect.left
            else :
                self.role.rect.left = self.goods_collision.rect.right
            self.role.x_vel = 0


    def y_collide(self):
        self.goods_collision = pygame.sprite.spritecollideany(self.role, self.cpt1_group)
        if self.goods_collision:
            if self.role.rect.bottom < self.goods_collision.rect.bottom:
                self.role.rect.bottom = self.goods_collision.rect.top
            else:
                self.role.rect.top = self.goods_collision.rect.bottom
            self.role.y_vel = 0


    def draw(self,surface):
        surface.blit(self.image, (0, 0))
        surface.blit(self.soldier1.image,self.soldier1.rect)
        surface.blit(self.soldier2.image,self.soldier2.rect)
        surface.blit(self.prince.image,self.prince.rect)




        surface.blit(self.role.role_image,self.role.rect)
        self.draw_chat_board(self.judge,surface)



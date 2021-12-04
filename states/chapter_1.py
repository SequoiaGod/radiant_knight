import pygame
from sources import default,tools
from states import roles,goods,load_js,npc

class Cpt1:
    '''
        this is chapter one code
    '''
    def __init__(self):
        self.Cpt1_background()
        self.setup_role()
        self.cpt1_map = load_js.load_map('./states/chapter1.json')  # [{"x": 293, "y": 379, "width": 211, "height": 43}]
        tools.trans_pixis(self.cpt1_map)
        self.setup_goods()

        self.setup_npc()
        pygame.mixer.music.load('./data/sounds/cpt1.mp3')
        pygame.mixer.music.play(1,100)




    def Cpt1_background(self):
        self.image = pygame.image.load('./data/map/chapter_1.png')
        self.image = pygame.transform.scale(self.image,(default.SCREEN_WIDTH,default.SCREEN_HEIGHT))

        pass
    def setup_goods(self):
        self.cpt1_group = pygame.sprite.Group()
        for item in self.cpt1_map :
            self.cpt1_group.add(goods.Goods(item['x'],item['y'],item['width'],item['height']))
        print(self.cpt1_group)

    def setup_npc(self):
        self.soldier = npc.NPC(default.info[0])
        self.soldier.rect.x = 570
        self.soldier.rect.y = 414




    def setup_role(self):
        self.role = roles.Role()
        self.role.rect.x = 425
        self.role.rect.y = 660

    def Cpt1_play(self):
        pass

    def update(self, surface,keys):
        self.role.update(keys)
        self.update_position()
        self.draw(surface)

    def update_position(self):

        self.role.rect.x += self.role.x_vel
        self.x_collide()
        self.role.rect.y += self.role.y_vel

        self.y_collide()
        print(self.role.rect)

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
        surface.blit(self.soldier.image,self.soldier.rect)
        surface.blit(self.role.role_image,self.role.rect)



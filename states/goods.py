import pygame

class Goods(pygame.sprite.Sprite) :
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        # self.width = width
        # self.height = height
        self.image  = pygame.Surface((width,height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class item_gooods(pygame.sprite.Sprite) :
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


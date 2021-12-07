import pygame
from sources import tools,default
from states import load_js,chat_board

class NPC(pygame.sprite.Sprite):
    def __init__(self,name,info):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.info = info
        self.cpt1_mes = load_js.load_map('./states/cpt_1_mes.json')
        self.chat_mes = self.cpt1_mes[self.name]

        print(self.chat_mes)
        self.npc_image(self.info)

    def npc_image(self,info):
        self.image = tools.capture(info['path'],*info['location'],info['color'],info['width'],info['height'])
        #self.image = tools.capture('./data/roles/guard/2.png', 53, 0, 37, 48, (0, 0, 0), 48, 48)
        self.rect = self.image.get_rect()

    def npc_mes(self):

        pass


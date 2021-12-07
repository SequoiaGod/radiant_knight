import pygame
from sources import tools,default
from states import load_js,chat_board

class NPC(pygame.sprite.Sprite):
    def __init__(self,name,info,npc_pit):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.info = info
        self.npc_pit = npc_pit # this is npc profile picture
        self.npc_image(self.info)
        self.cpt1_mes = load_js.load_map('./states/cpt_1_mes.json')
        self.chat_mes = self.cpt1_mes[self.name]
        self.pre_time = 0
        print(self.chat_mes)
        self.npc_image(self.info)

    def npc_image(self,info_path):
        self.structure = []
        for info in info_path :
            self.image = tools.capture(info['path'],*info['location'],info['color'],info['width'],info['height'])
            self.structure.append(self.image)
        #self.image = tools.capture('./data/roles/guard/2.png', 53, 0, 37, 48, (0, 0, 0), 48, 48)

        self.role_index = 0
        self.role_image = self.structure[self.role_index]
        self.rect = self.role_image.get_rect()


    def update(self):
        self.time = pygame.time.get_ticks()

        if self.time - self.pre_time > 200 :
            self.pre_time = self.time
            self.pre_time = self.time
            self.role_index += 1
            self.role_index = self.role_index % 3

            self.role_image = self.structure[self.role_index]
        pass


import pygame
from sources import default

class Game :
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((default.SCREEN_WIDTH, default.SCREEN_HEIGHT))
        self.key = pygame.key.get_pressed()
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        # self.image = pygame.image.load('./data/map/chapter_1.png')
        # self.screen.blit(self.image,(0,0))
        # pygame.display.flip()

    def run(self,state):
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    exit()

                elif event.type == pygame.KEYUP:

                    self.key = pygame.key.get_pressed()
                    pass
                elif event.type == pygame.KEYDOWN:
                        self.key = pygame.key.get_pressed()

            state.update(self.screen,self.key)
            pygame.display.flip()
            self.clock.tick(60)



def capture(path,x,y,width,hight,color,real_width,real_heigh) :
    pict = pygame.image.load(path)
    img = pygame.Surface((width,hight))
    img.blit(pict,(0,0),(x,y,width,hight))
    img.set_colorkey(color)
    img = pygame.transform.scale(img,(real_width,real_heigh))
    return img

def trans_pixis(list) :
    for item in list:
        item['x'] = int(item['x'] * default.CPT1_PIXIS_X)
        item['y'] = int(item['y'] * default.CPT1_PIXIX_Y)
        item['width'] = int(item['width'] * default.CPT1_PIXIS_X)
        item['height'] = int(item['height'] * default.CPT1_PIXIX_Y)







# game = Game()
# game.run()
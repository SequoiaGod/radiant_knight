import pygame
from sources import default

class Game :
    def __init__(self,state_dict,state):
        pygame.init()
        screen = pygame.display.set_mode((default.SCREEN_WIDTH, default.SCREEN_HEIGHT))
        self.key = pygame.key.get_pressed()
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.state_dict = state_dict
        self.state = self.state_dict[state]
        # self.image = pygame.image.load('./data/map/chapter_1.png')
        # self.screen.blit(self.image,(0,0))
        # pygame.display.flip()

    def update_state(self):
        if self.state.finish:
            self.next_state = self.state.next
            self.state.finish = False
            self.state = self.state_dict[self.next_state]
        self.state.update(self.screen,self.key)



    def run(self):
        while True :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    exit()

                if self.state.next == 'load':

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.key = pygame.mouse.get_pressed()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        self.key = pygame.mouse.get_pressed()
                        print(self.key)
                        print(pygame.mouse.get_pos())

                else :
                    self.key = pygame.key.get_pressed()
                    if event.type == pygame.KEYUP:

                        self.key = pygame.key.get_pressed()
                        pass
                    elif event.type == pygame.KEYDOWN:
                            self.key = pygame.key.get_pressed()

            self.update_state()
            #state.update(self.screen,self.key)
            pygame.display.flip()
            self.clock.tick(60)



def capture(path,x,y,width,hight,color,real_width,real_heigh) :
    pict = pygame.image.load(path)
    img = pygame.Surface((width,hight))
    img.blit(pict,(0,0),(x,y,width,hight))
    img.set_colorkey(color)
    img = pygame.transform.scale(img,(real_width,real_heigh))
    return img

def trans_pixis(list,scale_x,scale_y) :
    for item in list:
        item['x'] = int(item['x'] * scale_x)
        item['y'] = int(item['y'] * scale_y)
        item['width'] = int(item['width'] * scale_x)
        item['height'] = int(item['height'] * scale_y)





# game = Game()
# game.run()
import pygame
from sources import tools,default
import main
class Gameover :
    def __init__(self):
        self.state_name = 'gameover'
        self.set_music = True
        self.finish = False
        self.next = 'menu'

        self.time = 0
        self.set_background()


    def set_background(self):
        '''
        set up the background of the gameover
        :return:
        '''
        self.image = pygame.image.load('./data/map/gameover.png')
        self.image = pygame.transform.scale(self.image, (default.SCREEN_WIDTH, default.SCREEN_HEIGHT))



    def update(self,surface,keys):
        self.draw(surface)
        if keys[pygame.K_a]:

            self.finish = True
            default.HERO_ITEM = {"pearls": 0, "sword": 0, "jewel": 0}
            default.piano_judge = False
            main.main()

        if self.set_music:
            self.set_music = False
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load('./data/sounds/gameover.mp3')
            pygame.mixer.music.play(-1)


    def draw(self,surface):
        surface.blit(self.image,(0,0))



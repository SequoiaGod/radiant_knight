import pygame
from sources import default,tools,setup
from states import roles,goods,load_js,npc,chat_board
import  main


class Cpt6 :

    def __init__(self):
        self.state_name = 'cpt6'
        self.set_music = True
        self.finish = False
        self.next = 'menu'

        self.time = 0
        self.Cpt6_background()





    def Cpt6_background(self):
        '''
        set up the background of the chapter_1
        :return:
        '''
        self.image = pygame.image.load('./data/map/chapter_6.png')
        self.image = pygame.transform.scale(self.image,(default.SCREEN_WIDTH,default.SCREEN_HEIGHT))


    def update(self,surface,keys):
        self.draw(surface)
        if self.time == 0:
            self.time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.time > 35000:

            self.time = 0
            self.finish = True
            default.HERO_ITEM = {"pearls": 0, "sword": 0, "jewel": 0}
            #default.piano_judge = False
            main.main()

        if self.set_music:
            self.set_music = False
            if default.piano_judge == False:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.music.load('./data/sounds/cpt6.mp3')
                pygame.mixer.music.play(-1)



    def draw(self,surface):
        surface.blit(self.image,(0,0))
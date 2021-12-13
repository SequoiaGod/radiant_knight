import pygame
from sources import tools,default
import time

class Chat :
    def __init__(self):
        self.chat_img()
        self.rect.x = 0
        self.rect.y = 520
        self.time = 0
        self.num_word = 0


    def chat_img(self):
        '''
        init the chat board image
        :return:
        '''
        self.img = tools.capture('./data/chat/chat_1.png',0,0,500,284,(0,0,0),default.SCREEN_WIDTH,200)
        self.rect = self.img.get_rect()
        self.font = pygame.font.Font("./font/word1.TTF", 18)
        #self.mes1 = self.font.render("There are increasing magic soldiers. I have no idea what to do in the future.", True, (255, 255, 255))


    def print_mes(self,mes,surface):
        '''
        draw  the words into the chat board
        :param mes:
        :param surface:
        :return:
        '''
        surface.blit(self.img, self.rect)
        self.mes1 = self.font.render(mes, True, (255, 255, 255))
        surface.blit(self.mes1, (default.CHAT_START_X , default.CHAT_START_Y))


    # def print_roll(self,surface):



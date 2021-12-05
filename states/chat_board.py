import pygame
from sources import tools

class Chat :
    def __init__(self):
        self.chat_img()


    def chat_img(self):
        self.img = tools.capture('./data/chat/chat_1.png',0,0,500,284,(0,0,0),900,200)
        self.rect = self.img.get_rect()
        self.font = pygame.font.Font("./font/word1.TTF", 35)
        self.mes1 = self.font.render("Hi Mr jun, welcome to new world!!!!  hey", True, (255, 255, 255))



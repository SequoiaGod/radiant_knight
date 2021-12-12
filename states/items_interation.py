from sources import  default
import pygame
from states import load_js



class Item :
    def __init__(self,name):
        self.name = name
        self.mes_list = load_js.load_map('./states/chat_mes.json')
        self.chat_mes = self.mes_list[self.name]
        self.attri = "item"
        pass







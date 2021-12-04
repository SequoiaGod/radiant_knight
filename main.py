import pygame
from sources import tools
from states import chapter_1

def main() :
    game = tools.Game()
    cpt1 = chapter_1.Cpt1()
    game.run(cpt1)




if __name__ == '__main__':
    main()


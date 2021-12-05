import pygame
from sources import tools
from states import chapter_1,menu_set,load_window

def main() :

    state_dict = {'menu': menu_set.Menu(),
                  'load': load_window.Load(),
                  'cpt1': chapter_1.Cpt1()}
    game = tools.Game(state_dict,'menu')
    # menu = menu_set.Menu()
    cpt1 = chapter_1.Cpt1()
    load = load_window.Load()
    game.run()




if __name__ == '__main__':
    main()


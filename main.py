import pygame
from sources import tools
from states import chapter_1,menu_set,load_window,chapter_2

def main() :
    '''
    This function is set to start entire game
    :return:
    '''
    # state_dict stores all of state. such as chapter1 and start menu.
    state_dict = {'menu': menu_set.Menu(),
                  'load': load_window.Load(),
                  'cpt1': chapter_1.Cpt1(),
                  'cpt2': chapter_2.Cpt_2()}
    game = tools.Game(state_dict,'menu')
    # menu = menu_set.Menu()
    cpt1 = chapter_1.Cpt1()
    load = load_window.Load()
    game.run()




if __name__ == '__main__':
    main()


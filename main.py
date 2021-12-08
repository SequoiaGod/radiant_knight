import pygame
from sources import tools,default
from states import chapter_1,menu_set,load_window,chapter_2,chapter_3,chapter_4,chapter_5

def main() :
    '''
    This function is set to start entire game
    :return:
    '''
    # state_dict stores all of state. such as chapter1 and start menu.
    default.load_picture()
    state_dict = {'menu': menu_set.Menu(),
                  'load': load_window.Load(),
                  'cpt1': chapter_1.Cpt1(),
                  'cpt2': chapter_2.Cpt2(),
                  'cpt3': chapter_3.Cpt3(),
                  'cpt4': chapter_4.Cpt4(),
                  'cpt5': chapter_5.Cpt5(),
                  }
    game = tools.Game(state_dict,'menu')
    # menu = menu_set.Menu()
    cpt1 = chapter_1.Cpt1()
    load = load_window.Load()
    game.run()




if __name__ == '__main__':
    main()


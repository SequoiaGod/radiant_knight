from sources import tools

SCREEN_WIDTH = 1080# 1080
SCREEN_HEIGHT = 720 # 720
HERO_SPEED = 3
info = [[{'path': './data/roles/guard/2.png','location':(53, 0, 37, 48),'color':(0,0,0),'width':48,'height':48},
        {'path': './data/roles/guard/2.png','location':(3, 0, 37, 48),'color':(0,0,0),'width':48,'height':48},
         {'path': './data/roles/guard/2.png','location':(101, 0, 37, 48),'color':(0,0,0),'width':48,'height':48}],
        [{'path': './data/roles/prince/2.png','location':(53, 0, 37, 48),'color':(0,0,0),'width':48,'height':48},
         {'path': './data/roles/prince/2.png','location':(3, 0, 37, 48),'color':(0,0,0),'width':48,'height':48},
         {'path': './data/roles/prince/2.png','location':(101, 0, 37, 48),'color':(0,0,0),'width':48,'height':48}]]

HERO_SIZE =32

CPT1_PIXIS_X = 64.286
CPT1_PIXIS_Y = 57.143

CPT2_PIXIS_X = 47.36
CPT2_PIXIS_Y = 42.1


CHAT_START_X = 50
CHAT_START_Y = 570
# x = 0.986 47
# y = 0.877 42
HUMAN_PICTURE = []
pict_size = 70
HUMAN_PICT_WIDTH = 940
HUMAN_PICT_HEIGHT = 630
def load_picture() :
        '''
        this fuction is set for all the profile picture of character
        :return:
        '''
        HUMAN_PICTURE.append(tools.capture('./data/roles/guard/1.png',0,0,144,144,(0,0,0),pict_size,pict_size))
        HUMAN_PICTURE.append(tools.capture('./data/roles/prince/1.png',0,0,144,144,(0,0,0),pict_size,pict_size))
        HUMAN_PICTURE.append(tools.capture('./data/roles/knight/1.png',0,0,144,144,(0,0,0),pict_size,pict_size))






from sources import tools

SCREEN_WIDTH = 1080  # 1080
SCREEN_HEIGHT = 720  # 720
HERO_SPEED = 3
HERO_SIZE = 32
HERO_SPEED = 3
HERO_ITEM = {"pearls": 0, "sword": 0, "jewel": 0}
ITEM_LIST = []
HUMAN_PICTURE = []
CPT4_ITEM = []
CPT4_ITEM_SIZE = 26
# info :  the picture of npc gesture
info = [[{'path': './data/roles/guard/2.png', 'location': (53, 0, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/guard/2.png', 'location': (3, 0, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/guard/2.png', 'location': (101, 0, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE}],
        [{'path': './data/roles/prince/2.png', 'location': (53, 0, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/prince/2.png', 'location': (3, 0, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/prince/2.png', 'location': (101, 0, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE}],
        [{'path': './data/roles/mage/2.png', 'location': (53, 96, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/mage/2.png', 'location': (3, 96, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/mage/2.png', 'location': (101, 96, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE}],

        [{'path': './data/roles/Devil_king/2.png', 'location': (53, 0, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/Devil_king/2.png', 'location': (3, 0, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/Devil_king/2.png', 'location': (101, 0, 37, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE}],
    [{'path': './data/roles/mage/2.png', 'location': (53,48,38,48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/mage/2.png', 'location': (3,48,38,48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE},
         {'path': './data/roles/mage/2.png', 'location': (101, 48, 38, 48), 'color': (0, 0, 0), 'width': HERO_SIZE,
          'height': HERO_SIZE}
     ]
        ]

CPT1_PIXIS_X = 33.75
CPT1_PIXIS_Y = 30

CPT2_PIXIS_X = 33.75
CPT2_PIXIS_Y = 30

CHAT_START_X = 130
CHAT_START_Y = 570
# x = 0.986 47
# y = 0.877 42

pict_size = 70  # The size of profile picture of character
HUMAN_PICT_WIDTH = 40  # This is the location of character profile picture
HUMAN_PICT_HEIGHT = 530

HERO_PICT_WIDTH = 40
HERO_PICT_HEIGHT = 630


def load_picture():
    '''
        this fuction is set for all the profile picture of character
        :return:
        '''
    HUMAN_PICTURE.append(tools.capture('./data/roles/guard/1.png', 0, 0, 144, 144, (0, 0, 0), pict_size, pict_size))
    HUMAN_PICTURE.append(tools.capture('./data/roles/prince/1.png', 0, 0, 144, 144, (0, 0, 0), pict_size, pict_size))
    HUMAN_PICTURE.append(tools.capture('./data/roles/knight/1.png', 0, 0, 144, 144, (0, 0, 0), pict_size, pict_size))
    HUMAN_PICTURE.append(tools.capture('./data/roles/mage/1.png', 0, 0, 144, 144, (0, 0, 0), pict_size, pict_size))
    HUMAN_PICTURE.append(tools.capture('./data/roles/Devil_king/1.png', 0, 0, 144, 144, (0, 0, 0), pict_size, pict_size))
    ITEM_LIST.append(tools.capture2('./data/item/letter.png', 110, 76, 1190, 787, 800, 530))
    ITEM_LIST.append(tools.capture2('./data/item/stone.png', 0, 0, 1250, 717, 800, 460))
    ITEM_LIST.append(tools.capture2('./data/item/letter3.png', 0, 0, 800, 535, 800, 535))
    ITEM_LIST.append(tools.capture2('./data/item/letter2.png', 110, 76, 1190, 787, 800, 530))
    CPT4_ITEM.append(tools.capture('./data/goods/item.png', 0, 0, 46, 46, (0, 0, 0), CPT4_ITEM_SIZE, CPT4_ITEM_SIZE))
    CPT4_ITEM.append(tools.capture('./data/goods/item.png', 674, 0, 46, 46, (0, 0, 0), CPT4_ITEM_SIZE, CPT4_ITEM_SIZE))
    CPT4_ITEM.append(tools.capture('./data/goods/item.png', 528, 0, 46, 46, (0, 0, 0), CPT4_ITEM_SIZE, CPT4_ITEM_SIZE))

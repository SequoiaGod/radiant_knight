import pygame
from sources import tools,default




class Menu :
    def __init__(self):
        self.finish = False
        self.next = 'load'
        self.setup_background()
        self.judge = False



    def setup_background(self):
        self.setting_image = tools.capture2('./data/menu/setting.png', 105, 82, 1211, 766, 800, 506) # tools.capture('./data/menu/setting.png',0,0,1352,896,(255,255,255),800,531)#
        self.image = tools.capture('./data/menu/background.png',0,0,816,624,(0,0,0),default.SCREEN_WIDTH,default.SCREEN_HEIGHT)
        self.name = tools.capture('./data/menu/name.png',0,0,723,151,(0,0,0),723,151)
        self.cir = pygame.image.load('./data/menu/cir.png') # tools.capture('./data/menu/cir.png',0,0,293,339,(0,0,0),293,335)
        #self.cursor = tools.capture('./data/menu/cursor.png',0,0,150,148,(0,0,0),100,100)
        '''This is X signal'''
        self.xsignal_button = pygame.sprite.Sprite()
        self.xsignal_button.image = tools.capture('./data/menu/x_signal.png',0,0,400,400,(0,0,0),100,100)
        self.x_rect = self.xsignal_button.image.get_rect()
        self.x_rect.x,self.x_rect.y = (780,75)
        self.xsignal_button.rect = self.x_rect

        ''' This is start button'''
        self.start_button = pygame.sprite.Sprite()
        self.start_button.image = tools.capture('./data/menu/start01.png',0,0,222,85,(0,0,0),222,85)
        #self.start_button.image = pygame.image.load('./data/menu/start.png')
        rect = self.start_button.image.get_rect()
        rect.x,rect.y = (440,240)
        self.start_button.rect = rect

        '''This is control button'''
        self.control_button = pygame.sprite.Sprite()
        self.control_button.image = tools.capture('./data/menu/control01.png',0,0,222,85,(0,0,0),222,85)
        control_rect = self.control_button.image.get_rect()
        control_rect.x, control_rect.y = (440,350)
        self.control_button.rect = control_rect

        '''This is exit button'''
        self.exit_button = pygame.sprite.Sprite()
        self.exit_button.image = tools.capture('./data/menu/exit01.png',0,0,222,85,(0,0,0),222,85)
        exit_rect = self.exit_button.image.get_rect()
        exit_rect.x, exit_rect.y = (440,450)
        self.exit_button.rect = exit_rect


        pass
    def draw_setting(self,surface,judge):


        if judge:
            surface.blit(self.setting_image,(100, 75))
            surface.blit(self.xsignal_button.image, self.xsignal_button.rect)
    def update_info(self,keys):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        if keys[0]:
            if self.start_button.rect.collidepoint(self.mouse_x,self.mouse_y) : # choose start button
                self.finish = True
            elif self.control_button.rect.collidepoint(self.mouse_x,self.mouse_y) : # choose control button
                self.judge = True

                pass
            elif self.exit_button.rect.collidepoint(self.mouse_x,self.mouse_y) : # choose exit button
                exit()
            elif self.xsignal_button.rect.collidepoint(self.mouse_x,self.mouse_y) :
                self.judge = False

    def update(self,surface,keys):
        self.update_info(keys)
        surface.blit(self.image,(0,0))
        surface.blit(self.name,(180,0))
        surface.blit(self.cir,(400,220))
        surface.blit(self.start_button.image,self.start_button.rect)
        surface.blit(self.control_button.image,self.control_button.rect)
        surface.blit(self.exit_button.image,self.exit_button.rect)
        self.draw_setting(surface,self.judge)

        #surface.blit(self.cursor,(280,250))

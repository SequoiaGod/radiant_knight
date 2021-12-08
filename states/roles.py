import pygame
from sources import tools,default


class Role(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.role_img()
        self.role_velocity()
        self.time_tools()


    def role_img(self):
        self.structure = []
        self.left_structure = []
        self.right_structure = []
        self.up_structure = []
        self.down_structure = []
        self.flag = 0
        self.stop_structure =[]
        self.current_structure = []
        self.img_rect = [( 3, 0, 38, 48),
                         (53,0,38,48),
                         (101,0,38,48),
                         (3,48,38,48),
                         (53,48,38,48),
                         (101, 48, 38, 48),
                         (3, 96, 38, 48),
                         (53, 96, 38, 48),
                         (101, 96, 38, 48),
                         (3, 144, 38, 48),
                         (53, 144, 38, 48),
                         (101, 144, 38, 48),
        ]
        for rect in self.img_rect :
            if self.flag //3 == 0 :
                self.down_structure.append(tools.capture('./data/roles/knight/2.png', *rect,(0,0,0), default.HERO_SIZE, default.HERO_SIZE))

            elif self.flag //3 ==1 :
                self.left_structure.append(tools.capture('./data/roles/knight/2.png', *rect,(0,0,0), default.HERO_SIZE, default.HERO_SIZE))

            elif self.flag //3 ==2 :
                self.right_structure.append(tools.capture('./data/roles/knight/2.png', *rect,(0,0,0), default.HERO_SIZE, default.HERO_SIZE))

            elif self.flag //3 ==3 :
                self.up_structure.append(tools.capture('./data/roles/knight/2.png', *rect,(0,0,0), default.HERO_SIZE, default.HERO_SIZE))
            self.flag +=1
        self.stop_structure.append(self.up_structure[1])
        self.stop_structure.append(self.up_structure[1])
        self.stop_structure.append(self.up_structure[1])
        self.current_structure = self.stop_structure
        self.structure.append(tools.capture('./data/roles/knight/2.png', 3, 0, 38, 48,(0,0,0), 48, 48))
        self.role_index = 0
        self.role_image = self.structure[self.role_index]
        self.rect = self.role_image.get_rect()
        pass

    def role_velocity(self):
        self.x_vel = 0
        self.y_vel = 0

    def time_tools(self):
        self.pre_time = 0


    def update(self, keys):
        self.time = pygame.time.get_ticks()

        if keys[pygame.K_LEFT]:
            self.x_vel = -default.HERO_SPEED
            self.y_vel = 0
            self.current_structure = self.left_structure
        if keys[pygame.K_UP]:
            self.x_vel = 0
            self.y_vel = -default.HERO_SPEED
            self.current_structure = self.up_structure
        if keys[pygame.K_DOWN]:
            self.x_vel = 0
            self.y_vel = default.HERO_SPEED
            self.current_structure = self.down_structure

        if keys[pygame.K_RIGHT]:
            self.x_vel = default.HERO_SPEED
            self.y_vel = 0
            self.current_structure = self.right_structure

        if not (keys[pygame.K_LEFT]) and not (keys[pygame.K_RIGHT]) and not (keys[pygame.K_UP]) and not (keys[pygame.K_DOWN]) :
            self.x_vel = 0
            self.y_vel = 0


        if self.time - self.pre_time >100 :
            self.pre_time = self.time
            self.role_index += 1
            self.role_index  = self.role_index % 3

            self.role_image = self.current_structure[self.role_index]
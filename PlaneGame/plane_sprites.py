import pygame

# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 定义刷新帧率的常量
FRAME_PER_SEC = 60

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self,image_name,speed=1):
        # 调用父类的初始化方法
        super().__init__()
        #定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    # 重写父类update方法
    def update(self):
        # 在屏幕的垂直放心上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类的方法实现精灵的创建
        super().__init__("./images/background.png")
        # 2.判断是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类的方法实现
        super().update()
        # 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方

        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y=-SCREEN_RECT.height
import pygame
from plane_sprites import *
# 模块初始化
pygame.init()

# 创建时钟对象
clock= pygame.time.Clock()


# 创建主窗口
game_rect = pygame.Rect(0,0,480,700)
screen = pygame.display.set_mode(game_rect.size)


# 游戏的背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

#英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(200,850))
# 统一绘制，调用update方法
pygame.display.update()

# 1.定义rect记录飞机的位置
hero_rect = pygame.Rect(200,500,102,126)

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)

# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)


# 游戏循环正式游戏开启
while True:
    clock.tick(60)
    # 2. 修改飞机的位置
    hero_rect.y -= 2
    if hero_rect.bottom<=0:
        hero_rect.y=game_rect.bottom
    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0,0))
    screen.blit(hero,hero_rect)

    # 让精灵组调用两个方法，update和draw方法
    enemy_group.update()
    enemy_group.draw(screen)

    # 4. 调用update方法更新显示
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出游戏
            pygame.quit()
            # 直接退出程序
            exit()


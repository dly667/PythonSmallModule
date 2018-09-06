import pygame
#初始化
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

# 1.定义rect记录飞机的位置
hero_rect = pygame.Rect(200,500,102,126)

pygame.display.update()
while True:
    clock.tick(60)
    # 2. 修改飞机的位置
    hero_rect.y -= 2

    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0,0))
    screen.blit(hero,hero_rect)

    # 4. 调用update方法更新显示
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#退出
pygame.quit()
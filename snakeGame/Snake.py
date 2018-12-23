#--coding:utf-8--
import pygame
import random

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
lime_green = (50, 205, 50)
other_green = (0, 250, 154)
pink = (255,204,255)
bright_red = (255,153,153)

pygame.mixer.pre_init(44100,16,2,4096)

pygame.init()


width = 100
height = 100
x = 150
y = 170


screenwidth = (650)
screenheight = (650)
screen = pygame.display.set_mode((screenwidth, screenheight))







pygame.display.set_caption("SnakebyDan")
pygame.display.update()
clock = pygame.time.Clock()
# font = pygame.font.SysFont("simhei", 40)
font = pygame.font.Font("./simhei.ttf", 40)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])



pygame.mixer.music.load("snek.wav")
pygame.mixer.music.play(-1)

def plot_snake(screen, color, snke_list, snake_size):
    for x,y in snke_list:
        pygame.draw.rect(screen, lime_green, [x, y, snake_size, snake_size])

def start_screen():
    exitgame = False
    while not exitgame:
        screen.fill(pink)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        click2 = pygame.mouse.get_pressed()

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, other_green,(150,450,100,50))
            if click[0] == 1:
                pygame.mixer.music.stop()
                gameloop()
        else:
            pygame.draw.rect(screen, lime_green,(150,450,100,50))

        pygame.draw.rect(screen, red,(440,450,100,50))
        if click2[0] == 1:
            pygame.quit()

        text_screen("欢迎来玩耍贪吃蛇", black, 80, 100)
        text_screen("点击绿色开始", black, 110, 175)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True


            pygame.display.update()
            clock.tick(45)



#game loop#
def gameloop():
    exitgame = False
    gameover = False
    snake_x = 45
    snake_y = 55
    snake_size = 25
    velocity_x = 0
    velocity_y = 0
    snke_list = []
    snke_length = 1
    fps = 60
    food_x = random.randint(20, screenwidth/2)
    food_y = random.randint(20, screenheight/2)
    score = 0
    init_velocity = 5
    food_x = random.randint(20, screenwidth/2)
    food_y = random.randint(20, screenheight/2)
    food_size = 24
    with open("Highscore.txt", "r") as f:
        Highscore = f.read()

    while not exitgame:
        if gameover:
            with open("Highscore.txt", "w") as f:
                f.write(str(Highscore))
            screen.fill(pink)
            text_screen("游戏结束！按R继续", red, 70, 90)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pygame.mixer.music.stop()
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score+=24



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                score +=10
                pygame.mixer.music.load("8bitpickup.wav")
                pygame.mixer.music.play()
                food_x = random.randint(20, screenwidth/2)
                food_y = random.randint(20, screenheight/2)
                snke_length +=5
                if score>int(Highscore):
                    Highscore = score


            screen.fill(black)
            text_screen("分数: "+ str(score) + " 最高分: "+str(Highscore), white, 5, 5)
            pygame.draw.rect(screen, red, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snke_list.append(head)

            if len(snke_list)>snke_length:
                del snke_list[0]

            if head in snke_list[:-1]:
                gameover = True
                pygame.mixer.music.load("Gameover.mp3")
                pygame.mixer.music.play()


            if snake_x<0 or snake_x>screenwidth or snake_y<0 or snake_y>screenheight:
                gameover = True
                pygame.mixer.music.load("Gameover.mp3")
                pygame.mixer.music.play()

            plot_snake(screen, black, snke_list, snake_size)
        clock.tick(fps)

        pygame.display.update()
        pygame.init()

    pygame.quit()

start_screen()

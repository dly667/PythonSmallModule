import pygame, sys, random

skier_images = ["./bg_img/skier_down.png", "./bg_img/skier_right1.png", "./bg_img/skier_right2.png",
                 "./bg_img/skier_left2.png", "./bg_img/skier_left1.png"]     # 将可能用到的图片列表化

class SkierClass(pygame.sprite.Sprite):  # 创建滑雪者
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # 基类的init方法
        self.image = pygame.image.load("./bg_img/skier_down.png") # 这个是滑雪者的美照。
        self.rect = self.image.get_rect() # 用于获得Image的矩形大小
        self.rect.center = [320, 100]  # 指定矩形的中心位置
        self.angle = 0

    def turn(self, direction):				# 滑雪者 转向函数 其中的direction参数是指定滑雪者移动的方向和程度（点击两次右键比一次右键滑动的幅度要大，一会自己试着运行一下试试。）
        self.angle = self.angle + direction		#滑雪者当前的移动速度
        if self.angle < -2:  self.angle = -2   # 用于将滑雪者的移动方式固定到这五个方式当中
        if self.angle >  2:  self.angle =  2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])	#这个时候滑雪者应该有的姿态图片。
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]	#滑雪者的速度。
        return speed

    def move(self, speed): 			#滑雪者左右移动
        self.rect.centerx = self.rect.centerx + speed[0]	#滑雪者所在位置
        if self.rect.centerx < 20:  self.rect.centerx = 20	# 滑雪者所在位置不应该超过的最大最小值。
        if self.rect.centerx > 620: self.rect.centerx = 620

class ObstacleClass(pygame.sprite.Sprite):	#创建书和小旗
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file	#image_file可能是树或者小旗
        self.image = pygame.image.load(image_file)	#载入当前的图片
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def scroll(self, terrainPos):	#场景上滚，造成下滑假象。
        self.rect.centery = self.location[1] - terrainPos

def create_map(start, end): 	# 创建一个窗口，包含随机的树和小旗
    obstacles = pygame.sprite.Group() # 创建独立运动的组织
    locations = []
    gates = pygame.sprite.Group()
    for i in range(10):
        row = random.randint(start, end) #获得随机数在 start-end之间
        col = random.randint(0, 9)
        location  = [col * 64 + 20, row * 64 + 20] # 确定所在位置
        if not (location in locations): # 如果上面定义的物体不在已经确定属性（位置等参数）的物体里面。
            locations.append(location)
            type = random.choice(["tree", "flag"])#随机选择是树还是小旗
            if type == "tree": img = "./bg_img/skier_tree.png"	#选择相应的图片
            elif type == "flag":  img = "./bg_img/skier_flag.png"
            obstacle = ObstacleClass(img, location, type)		#将上面的形成的物体添加到游戏
            obstacles.add(obstacle)		
    return obstacles

def animate(): 	# 如果发生移动就重新绘制屏幕
    screen.fill([255, 255, 255])	#指定背景颜色 （RGB）
    pygame.display.update(obstacles.draw(screen))#这个函数就pygame.display.flip的优化版本。它只允许屏幕的一部分更新，而不是整个区域。如果没有参数传递它更新整个表面积就像pygame.display.flip()一样。
    screen.blit(skier.image, skier.rect)# 用于绘制位图 在屏幕的skier.rect位置绘制skier.image
    screen.blit(score_text, [10, 10])
    pygame.display.flip()

def updateObstacleGroup(map0, map1):  # 切换到场景的下一屏
    obstacles = pygame.sprite.Group()
    for ob in map0:  obstacles.add(ob)
    for ob in map1:  obstacles.add(ob)
    return obstacles

pygame.init()        #初始化pygame的所有模块
#pygame.mixer.init()  # 初始化混音部分 进行声音的加载和播放---播放音频之用
#pygame.mixer.music.load("./bg_music/bg_music.mp3")  # 将会加载这一个音乐的文件名并且准备播放！
#pygame.mixer.music.set_volume(0.3)#设置音乐 的音量参数之在 0-1之间
#pygame.mixer.music.play(-1) #这将播放载入的音乐流。如果音乐已经播放，它就会重新启动。其中的参数时控制音乐播放的次数。如果是-1的话就是无限重复播放。
screen = pygame.display.set_mode([640,640])# 用于初始化窗口，其中的参数就是分辨率
clock = pygame.time.Clock()# 载入监听时间的模块 clock在下面还可以看到 clock.tick等方法
skier = SkierClass() # 初始化SkierClass对象
speed = [0, 6]
map_position = 0
points = 0
map0 = create_map(20, 29)
map1 = create_map(10, 19)
activeMap = 0

obstacles = updateObstacleGroup(map0, map1)

font = pygame.font.Font(None, 50)

while True:
    clock.tick(30)		# 每秒更新30次图形 ---这就是帧率。
    for event in pygame.event.get():    # 检查按键或者窗口是否关闭
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed)			# 移动滑雪者
    map_position += speed[1]		# 滚动场景

    if map_position >=640 and activeMap == 0: 		# 从场景的一个窗口切换到下一个窗口
        activeMap = 1
        map0 = create_map(20, 29)
        obstacles = updateObstacleGroup(map0, map1)
    if map_position >=1280 and activeMap == 1:
        activeMap = 0
        for ob in map0:
            ob.location[1] = ob.location[1] - 1280
        map_position = map_position - 1280
        map1 = create_map(10, 19)
        obstacles = updateObstacleGroup(map0, map1)

    for obstacle in obstacles:
        obstacle.scroll(map_position)

    hit =  pygame.sprite.spritecollide(skier, obstacles, False)		# 检查是否碰到树或者小旗。
    if hit:
        if hit[0].type == "tree" and not hit[0].passed:
            points = points - 100
            skier.image = pygame.image.load("./bg_img/skier_crash.png")
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.load("./bg_img/skier_down.png")
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == "flag" and not hit[0].passed:
            points += 10
            obstacles.remove(hit[0])
	#显示得分
    score_text = font.render("Score: " +str(points), 1, (0, 0, 0))
    animate()

import random
import pygame
####################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Avoid Fucking Shit!!!") # 게임 이름

# FPS
clock = pygame.time.Clock()
####################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경만들기
background = pygame.image.load("C:\\Users\\MasterAwmp\\Desktop\\python.directory\\NadoCoding_1\\pygame_basic\\background.png")

# 캐릭터 만들기
character = pygame.image.load("C:\\Users\\MasterAwmp\\Desktop\\python.directory\\NadoCoding_1\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 10

# 똥 만들기
shit = pygame.image.load("C:\\Users\\MasterAwmp\\Desktop\\python.directory\\NadoCoding_1\\pygame_basic\\enemy.png")
shit_size = shit.get_rect().size
shit_width = shit_size[0]
shit_height = shit_size[1]
shit_x_pos = random.randint(0, screen_width - shit_width)
shit_y_pos = 0
shit_speed = 10

running = True
while running:
    dt = clock.tick(60)
    
    # 2. 이벤트 처리 (키보드, 마우스 등)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
    # 3. 게임 캐릭터 위치 정의
    
    character_x_pos += to_x
    
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    shit_y_pos += shit_speed
    
    if shit_y_pos > screen_height:
        shit_y_pos = 0
        shit_x_pos = random.randint(0, screen_width - shit_width)
    
    # 4. 충돌 처리
    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    shit_rect = shit.get_rect()
    shit_rect.left = shit_x_pos
    shit_rect.top = shit_y_pos
    
    if character_rect.colliderect(shit_rect):
        print("충돌했어요")
        running = False
           
    # 5. 화면에 그리기
    
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(shit, (shit_x_pos, shit_y_pos))
    
    pygame.display.update()
    
pygame.quit()
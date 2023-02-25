import pygame # 파이게임이 잘 설치되었는지 확인

pygame.init() # 초기화 작업 (반드시 해야함)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Taero Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\MasterAwmp\\Desktop\\python.directory\\NadoCoding_1\\pygame_basic\\background.png")
# 탈출 문자 처리로 역슬래쉬를 2개씩 해주거나 그냥 슬래쉬 1개를 해준다.

# 이벤트 루프(창이 꺼지지 않고 표시되도록 하는 기능)
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 파이게임 사용 위해서는 무조건 적어야 하는 이벤트 루프, 프로그램이 종료되지 않도록 대기하는 것, 키보드나 마우스로 입력한 내용을 수행받아 화면 상에 출력해줌
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가? 예) 화면 우측 상단 x 버튼으로 종료하였을 때
            running = False # 게임이 진행 중이 아님
    
    # screen.fill((0, 0, 255)) # RGB값으로 화면 색 채우기
    screen.blit(background, (0,0)) # 배경 그리기

    pygame.display.update() # 매 프레임마다 화면에 배경을 그려주는 동작을 취해줘야 함 / 게임화면을 다시 그리기!
    
# pygame 종료
pygame.quit()
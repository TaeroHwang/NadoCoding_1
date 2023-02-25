import pygame # 파이게임이 잘 설치되었는지 확인

pygame.init() # 초기화 작업 (반드시 해야함)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Taero Game") # 게임 이름

# 이벤트 루프(창이 꺼지지 않고 표시되도록 하는 기능)
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 파이게임 사용 위해서는 무조건 적어야 하는 이벤트 루프, 프로그램이 종료되지 않도록 대기하는 것, 키보드나 마우스로 입력한 내용을 수행받아 화면 상에 출력해줌
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가? 예) 화면 우측 상단 x 버튼으로 종료하였을 때
            running = False # 게임이 진행 중이 아님

# pygame 종료
pygame.quit()
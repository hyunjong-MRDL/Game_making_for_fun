import os
import pygame
import numpy as np

MAP_SIZE = 25
CELL_SIZE = 15
WINDOW_SIZE = (MAP_SIZE * CELL_SIZE, MAP_SIZE * CELL_SIZE)

COLORS = {
    0: (150, 200, 150),  # 통로 (연한 녹색)
    1: (255, 0, 0),      # 포켓몬 센터 (빨강)
    2: (0, 0, 255),      # 상점 (파랑)
    3: (255, 165, 0),    # NPC 집 (주황)
    4: (128, 0, 128),    # 관장 체육관 (보라)
    5: (0, 100, 0),      # 가로수 (진한 녹색)
}

game_map = np.zeros((MAP_SIZE, MAP_SIZE), dtype=int)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pokemon Map Editor")

def draw_map():
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            cell_value = game_map[y, x]
            color = COLORS.get(cell_value, (0, 0, 0))
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

running = True
object_to_place = 1  # 현재 배치할 객체 (1: 포켓몬 센터, 2: 상점)
dragging = False     # 드래그 상태 변수

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 마우스 클릭/드래그 이벤트
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging = True
            mouse_x, mouse_y = event.pos
            map_x = mouse_x // CELL_SIZE
            map_y = mouse_y // CELL_SIZE
            if 0 <= map_x < MAP_SIZE and 0 <= map_y < MAP_SIZE:
                game_map[map_y, map_x] = object_to_place
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
        
        elif event.type == pygame.MOUSEMOTION and dragging:
            mouse_x, mouse_y = event.pos
            map_x = mouse_x // CELL_SIZE
            map_y = mouse_y // CELL_SIZE
            if 0 <= map_x < MAP_SIZE and 0 <= map_y < MAP_SIZE:
                game_map[map_y, map_x] = object_to_place

        # 마우스 오른쪽 클릭은 드래그 없이 단일 클릭으로 유지
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_x, mouse_y = event.pos
            map_x = mouse_x // CELL_SIZE
            map_y = mouse_y // CELL_SIZE
            if 0 <= map_x < MAP_SIZE and 0 <= map_y < MAP_SIZE:
                game_map[map_y, map_x] = 0
        
        # 키보드 입력
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                object_to_place = 1
                print("현재 배치할 객체: 포켓몬 센터 (1)")
            elif event.key == pygame.K_2:
                object_to_place = 2
                print("현재 배치할 객체: 상점 (2)")
            elif event.key == pygame.K_3:
                object_to_place = 3
                print("현재 배치할 객체: NPC 집 (3)")
            elif event.key == pygame.K_4:
                object_to_place = 4
                print("현재 배치할 객체: 관장 체육관 (4)")
            elif event.key == pygame.K_5:
                object_to_place = 5
                print("현재 배치할 객체: 가로수 (5)")
            elif event.key == pygame.K_s:
                curr_dir = os.path.dirname(os.path.abspath(__file__))
                map_file_path = os.path.join(curr_dir, "map_data.npy")
                np.save(map_file_path, game_map)
                print("맵이 'map_data.npy' 파일로 저장되었습니다.")
                
    screen.fill((255, 255, 255))
    draw_map()
    pygame.display.flip()

pygame.quit()
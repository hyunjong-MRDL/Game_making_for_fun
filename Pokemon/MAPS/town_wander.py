import os
import pygame
import numpy as np

MAP_SIZE = 25
CELL_SIZE = 15
WINDOW_SIZE = (MAP_SIZE * CELL_SIZE, MAP_SIZE * CELL_SIZE)
PLAYER_SPEED = 5

COLORS = {
    0: (150, 200, 150),  # 통로 (연한 녹색)
    1: (255, 0, 0),      # 포켓몬 센터 (빨강)
    2: (0, 0, 255),      # 상점 (파랑)
    3: (255, 165, 0),    # NPC 집 (주황)
    4: (128, 0, 128),    # 관장 체육관 (보라)
    5: (0, 100, 0),      # 가로수 (진한 녹색)
}

class Player:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.current_x = float(x)
        self.current_y = float(y)

    def draw(self, screen):
        center_x = self.current_x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.current_y * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, self.color, (int(center_x), int(center_y)), CELL_SIZE // 2 - 2)

    def move(self, dx, dy, game_map, dt):
        new_x_float = self.current_x + dx * PLAYER_SPEED * dt
        new_y_float = self.current_y + dy * PLAYER_SPEED * dt
        
        new_x_cell = int(round(new_x_float))
        new_y_cell = int(round(new_y_float))

        if (0 <= new_x_cell < MAP_SIZE and 
            0 <= new_y_cell < MAP_SIZE and 
            game_map[new_y_cell, new_x_cell] == 0):
            self.current_x = new_x_float
            self.current_y = new_y_float
            self.x = new_x_cell
            self.y = new_y_cell
        else:
            if dx > 0: self.current_x = int(self.current_x) + 0.999
            if dx < 0: self.current_x = int(self.current_x)
            if dy > 0: self.current_y = int(self.current_y) + 0.999
            if dy < 0: self.current_y = int(self.current_y)

curr_dir = os.path.dirname(os.path.abspath(__file__))
map_file_path = os.path.join(curr_dir, "map_data.npy")

try:
    game_map = np.load(map_file_path)
    if game_map.shape != (MAP_SIZE, MAP_SIZE):
        print("Warning: Loaded map has an incorrect size. Creating a new one.")
        game_map = np.zeros((MAP_SIZE, MAP_SIZE), dtype=int)
except FileNotFoundError:
    print("No map file found. Creating a new, empty map.")
    game_map = np.zeros((MAP_SIZE, MAP_SIZE), dtype=int)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Simple Pokemon Game")

def draw_map():
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            cell_value = game_map[y, x]
            color = COLORS.get(cell_value, (0, 0, 0))
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

pokemon_center = np.where(game_map==1)
start_pos = (pokemon_center[0].item()+1, pokemon_center[1].item()) if pokemon_center[0].size > 0 else (MAP_SIZE // 2, MAP_SIZE // 2)
player = Player(start_pos[0], start_pos[1])

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        keys = pygame.key.get_pressed()
        
        dx, dy = 0, 0
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
            
        dt = clock.tick(60) / 1000.0

        # Move the player if a key is held down
        if dx != 0 or dy != 0:
            player.move(dx, dy, game_map, dt)
    
    # --- Drawing the game state ---
    screen.fill((255, 255, 255))
    draw_map()
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
import os
import pygame
import numpy as np

MAP_SIZE = 25
CELL_SIZE = 15
WINDOW_SIZE = (MAP_SIZE * CELL_SIZE, MAP_SIZE * CELL_SIZE)
PLAYER_SPEED = 1

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

    def draw(self, screen):
        # Draw the player as a circle
        center_x = self.x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.y * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, self.color, (center_x, center_y), CELL_SIZE // 2 - 2)

    def move(self, dx, dy, game_map):
        new_x = self.x + dx
        new_y = self.y + dy

        # Check for valid movement
        if 0 <= new_x < MAP_SIZE and 0 <= new_y < MAP_SIZE:
            # Only allow movement to cells with a value of 0 (paths)
            if game_map[new_y, new_x] == 0:
                self.x = new_x
                self.y = new_y

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
pygame.display.set_caption("Pokemon Map Editor")

def draw_map():
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            cell_value = game_map[y, x]
            color = COLORS.get(cell_value, (0, 0, 0))
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

pokemon_center = np.where(game_map==1)
start_pos = (pokemon_center[0].item(), pokemon_center[1].item()+1)

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
            
        # Move the player if a key is held down
        if dx != 0 or dy != 0:
            player.move(dx, dy, game_map)
    
    # --- Drawing the game state ---
    screen.fill((255, 255, 255))
    draw_map()
    player.draw(screen)
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
import pygame
import sys

# Inisialisasi pygame
pygame.init()
pygame.joystick.init()

# Cek controller
if pygame.joystick.get_count() == 0:
    print("Controller tidak terdeteksi!")
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Controller Demo")

clock = pygame.time.Clock()

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
speed = 5

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Analog kiri (Xbox / PS)
    axis_x = joystick.get_axis(0)
    axis_y = joystick.get_axis(1)

    player_x += int(axis_x * speed)
    player_y += int(axis_y * speed)

    # Batas layar
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # Tombol (contoh: tombol A / X)
    if joystick.get_button(0):
        speed = 10
    else:
        speed = 5

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.display.flip()

pygame.quit()
sys.exit()

import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
ENEMY_SPAWN_RATE = 30  # Появление врагов каждые 30 кадров
SPEED = 5
ENEMY_MOVE_SPEED = 2

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Game")
font = pygame.font.Font(None, 36)

# Класс игрока
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, min(WIDTH - PLAYER_SIZE, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - PLAYER_SIZE, self.rect.y))

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# Класс врага
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE),
                                 random.randint(0, HEIGHT - ENEMY_SIZE),
                                 ENEMY_SIZE, ENEMY_SIZE)

    def move(self):
        # Двигаем врага случайным образом
        direction = random.choice([(ENEMY_MOVE_SPEED, 0), (-ENEMY_MOVE_SPEED, 0), (0, ENEMY_MOVE_SPEED), (0, -ENEMY_MOVE_SPEED)])
        self.rect.x += direction[0]
        self.rect.y += direction[1]
        # Ограничиваем движение врагов в пределах окна
        self.rect.x = max(0, min(WIDTH - ENEMY_SIZE, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - ENEMY_SIZE, self.rect.y))

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Основная функция игры
def main():
    clock = pygame.time.Clock()
    player = Player()
    enemies = []
    score = 0
    frame_count = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * SPEED
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * SPEED

        player.move(dx, dy)

        # Появление новых врагов
        frame_count += 1
        if frame_count % ENEMY_SPAWN_RATE == 0:
            enemies.append(Enemy())
            score += 1  # Увеличиваем счёт за каждого врага

        # Движение и проверка на столкновение
        for enemy in enemies:
            enemy.move()
            if player.rect.colliderect(enemy.rect):
                print(f"Game Over! Your score: {score}")
                running = False

        # Отрисовка
        screen.fill(WHITE)
        player.draw()
        for enemy in enemies:
            enemy.draw()

        # Отображение счётчика
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

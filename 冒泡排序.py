import pygame
import sys
from pygame.locals import *
import time

# 初始化
pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("冒泡排序可视化")

# 颜色
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# 数列和排序状态
original_numbers = [10, 5, 3, 8, 2, 6, 4, 7, 9, 1, 55, 23, 12, 34, 11, 22, 33, 44]
numbers = original_numbers.copy()
n = len(numbers)
sort_state = 'Idle'
last_swap_time = time.time()
delay = 0.01

# 字体设置
font = pygame.font.SysFont(None, 24)


def bubble_sort_step(numbers, n):
    global last_swap_time
    if time.time() - last_swap_time >= delay:
        swapped = False
        for i in range(n - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
                break
        if not swapped:
            return False
        last_swap_time = time.time()
    return True


def draw():
    screen.fill(BLACK)
    bar_width = screen_width / len(numbers)
    for i, num in enumerate(numbers):
        x = i * bar_width
        y = screen_height - (num / max(numbers) * screen_height)
        height = num / max(numbers) * screen_height
        pygame.draw.rect(screen, RED, (x, y, bar_width - 2, height))

        # 在矩形上方展示对应的值
        text_surf = font.render(str(num), True, WHITE)
        text_rect = text_surf.get_rect(center=(x + bar_width / 2, y - 10))
        screen.blit(text_surf, text_rect)

    pygame.display.flip()


# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_s:
                sort_state = 'Sorting'

    if sort_state == 'Sorting':
        if not bubble_sort_step(numbers, n):
            sort_state = 'Idle'

    draw()

pygame.quit()

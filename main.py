import pygame
import random
import os
import sys

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class LastScreen(pygame.sprite.Sprite):
    image = load_image("gameover.png")
    image_boom = load_image("boom.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = LastScreen.image
        self.pos_y = 0
        self.pos_x = -600
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect().move(
            self.size[0] * self.pos_x, self.size[1] * self.pos_y)

    def move_right(self):
        self.pos_x += 1
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)


running = True
last_screen = LastScreen(all_sprites)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if last_screen.pos_x < 0:
        last_screen.move_right()
    screen.fill('blue')
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(200)
pygame.quit()

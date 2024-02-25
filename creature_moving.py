import os
import sys
import pygame


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


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill("white")
all_sprites = pygame.sprite.Group()
image = load_image("creature.png")
sprite = pygame.sprite.Sprite(all_sprites)
sprite.image = image
screen.blit(image, (100, 100))
sprite.rect = sprite.image.get_rect().move(0, 0)
running = True
a = 0
b = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                a += 10
                sprite.rect = sprite.image.get_rect().move(a, b)
            if event.key == pygame.K_DOWN:
                b += 10
                sprite.rect = sprite.image.get_rect().move(a, b)
            if event.key == pygame.K_LEFT:
                a -= 10
                sprite.rect = sprite.image.get_rect().move(a, b)
            if event.key == pygame.K_UP:
                b -= 10
                sprite.rect = sprite.image.get_rect().move(a, b)
    screen.fill('white')
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()

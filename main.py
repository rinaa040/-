import pygame
import sys
import os

pygame.init()
size = width, height = 600, 95
screen = pygame.display.set_mode(size)
player = None

all_sprites = pygame.sprite.Group()

fps = 50
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


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


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.direction = 0
        self.image = load_image('car2.png')
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect().move(
            self.size[0] * pos_x, self.size[1] * pos_y)

    def move_right(self):
        self.direction = 0
        self.pos_x += 2
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)

    def move_left(self):
        self.direction = 1
        self.pos_x -= 2
        # self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect().move(
            self.pos_x, self.pos_y)


flag = False
running = True
player = Player(2, 0)
# generate_level(load_level('field.txt'))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
    if player.pos_x == 600 - player.size[0]:
        flag = True
        player.image = pygame.transform.flip(player.image, True, False)
    if player.pos_x == 0:
        flag = False
        player.image = pygame.transform.flip(player.image, True, False)
    if not flag:
        player.move_right()
    else:
        player.move_left()
    screen.fill('white')
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(50)
    pygame.display.flip()
pygame.quit()

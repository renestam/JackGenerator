from generator import generate
import pygame, images

wn_width, wn_height = 750, 750
window = pygame.display.set_mode((wn_width, wn_height))


def draw_images(images, size):
    for i in range(15):
        for j in range(15):
            img = pygame.transform.scale(images[i*15 + j], size)
            window.blit(img, (j*(wn_width/15), i*(wn_height/15)))

    pygame.display.update()

draw_images(images.bg_pygame, (50, 50))
draw_images(generate(images.rand_pygame, 110), (50, 50))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                draw_images(images.bg_pygame, (50, 50))
                draw_images(generate(images.rand_pygame, 110), (50, 50))
        
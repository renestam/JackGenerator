import pygame
from PIL import Image

bg_dir = 'Images/BG Images 2/'
bg_names = [str(i+1) + '.jpg' for i in range(225)]
bg_names.reverse()
bg_pygame = [pygame.image.load(bg_dir + i) for i in bg_names]

rand_dir = 'Images/Random Images/'
rand_names = [str(i) + '.jpg' for i in range(225)]
rand_pygame = [pygame.image.load(rand_dir + i) for i in rand_names]


def rename_files(files, old_dir, new_dir):
    for i in range(len(files)):
        img = Image.open(old_dir + files[i])
        img.save(new_dir + str(i) + '.jpg')

#rename_files(bg_names, bg_dir, 'Images/BG Images 2')
#rename_files(rand_names, rand_dir, 'Images/Random Images 2')
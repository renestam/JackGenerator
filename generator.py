import pygame, random


def generate(images, alpha):
    random.shuffle(images)

    for i in range(len(images)):
        images[i].set_alpha(alpha)

    return images

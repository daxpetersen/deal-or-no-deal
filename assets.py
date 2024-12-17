import pygame

def load_image(image_path):
    return pygame.image.load(image_path)

def load_sound(sound_path):
    return pygame.mixer.Sound(sound_path)

def load_music(music_path):
    pygame.mixer.music.load(music_path)

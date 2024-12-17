
import pygame

def display_welcome_message():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("The Price is Right")
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("Arial", 48)
    text = font.render("Welcome to 'The Price is Right'!", True, (0, 0, 0))
    screen.blit(text, (100, 250))
    pygame.display.flip()
    pygame.time.wait(2000)

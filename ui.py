import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GREEN, RED, FONT

class UI:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The Price is Right")
        self.clock = pygame.time.Clock()

    def draw_text(self, text, x, y, color=BLACK, font_size=36):
        font = pygame.font.SysFont("Arial", font_size)
        rendered_text = font.render(text, True, color)
        self.screen.blit(rendered_text, (x, y))

    def draw_button(self, text, x, y, width, height, color=GREEN):
        pygame.draw.rect(self.screen, color, (x, y, width, height))
        self.draw_text(text, x + 10, y + 10, WHITE)

    def wait_for_click_or_timeout(self, timeout_seconds):
        time_elapsed = 0
        while time_elapsed < timeout_seconds * 1000:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
            self.clock.tick(60)
            time_elapsed += self.clock.get_time()
        return False

    def display_contestant_bids(self, contestants):
        self.screen.fill(WHITE)
        y_position = 100
        for contestant in contestants:
            self.draw_text(f"{contestant.name} bids: ${contestant.bidding}", 100, y_position)
            y_position += 40
        pygame.display.flip()

    def display_vowel_selection(self, available_vowels):
        self.screen.fill(WHITE)
        y_position = 100
        for i, vowel in enumerate(available_vowels):
            self.draw_button(vowel, 100, y_position + i * 50, 100, 40)
        pygame.display.flip()

    def display_welcome_message(self):
        self.screen.fill(WHITE)
        self.draw_text("Welcome to The Price is Right!", 100, 250, BLACK, 48)
        pygame.display.flip()
        pygame.time.wait(2000)

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
pygame.font.init()
FONT = pygame.font.SysFont("Arial", 36)

def draw_text(screen, text, x, y, color=BLACK):
    rendered_text = FONT.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def wait_for_click_or_timeout(timeout_seconds):
    clock = pygame.time.Clock()
    time_elapsed = 0
    while time_elapsed < timeout_seconds * 1000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        clock.tick(FPS)
        time_elapsed += clock.get_time()

def spin_wheel():
    options = ["skip","vowel","consonant","free_guess"]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    spin_duration = 5000 
    start_time = pygame.time.get_ticks()
    current_option = random.choice(options)
    while pygame.time.get_ticks() - start_time < spin_duration:
        screen.fill(WHITE)
        draw_text(screen, "Spinning Wheel: " + current_option, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3, GREEN)
        pygame.display.flip()

        current_option = random.choice(options)
        clock.tick(10) 
    
    draw_text(screen, "Spinning Wheel: " + current_option, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3, GREEN)
    pygame.display.flip()
    wait_for_click_or_timeout(2) 
    return current_option

def select_letter(used_letters, letter_type, revealed_word):
    available_letters = [chr(i) for i in range(65, 91)] 
    available_letters = [l for l in available_letters if l not in used_letters]

    if letter_type == "consonant":
        vowels = ['A', 'E', 'I', 'O', 'U']
        available_letters = [l for l in available_letters if l not in vowels]  

    if letter_type == "vowel":
        vowels = ['A', 'E', 'I', 'O', 'U']
        available_letters = [l for l in available_letters if l in vowels] 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    selected_letter = None
    columns = 6 
    rows = len(available_letters) // columns + (1 if len(available_letters) % columns != 0 else 0)
    x_offset = 50 
    y_offset = 200  
    letter_width = 100 
    letter_height = 50

    while not selected_letter:
        screen.fill(WHITE)

        for i, letter in enumerate(available_letters):
            row = i // columns
            col = i % columns
            letter_x = x_offset + col * letter_width
            letter_y = y_offset + row * letter_height
            draw_text(screen, f"{letter}", letter_x, letter_y, BLACK)

        phrase_display = ' '.join([revealed_word[i] if revealed_word[i] != '_' else '_' for i in range(len(revealed_word))])
        draw_text(screen, "Phrase: " + phrase_display, 50, 50)
        draw_text(screen, "Click a letter or type it:", 50, 100)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                letter = event.unicode.upper()
                if letter in available_letters and letter not in revealed_word:
                    selected_letter = letter
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, letter in enumerate(available_letters):
                    row = i // columns
                    col = i % columns
                    letter_x = x_offset + col * letter_width
                    letter_y = y_offset + row * letter_height
                    if letter_x <= mouse_x <= letter_x + letter_width and letter_y <= mouse_y <= letter_y + letter_height:
                        selected_letter = letter
                        break

        clock.tick(FPS)
    return selected_letter

def get_free_guess_input(revealed_word):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    input_text = ''
    input_active = True

    while input_active:
        screen.fill(WHITE)
        phrase_display = ' '.join([revealed_word[i] if revealed_word[i] != '_' else '_' for i in range(len(revealed_word))])
        draw_text(screen, "Type the phrase (only where known letters aren't):", 50, 50)
        draw_text(screen, phrase_display, 50, 100)
        draw_text(screen, "Your input: " + input_text, 50, 150)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.unicode.isalpha() and len(input_text) < len(revealed_word):
                    input_text += event.unicode.upper()

        clock.tick(FPS)
    return input_text.upper()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("The Price is Right")
    
    players = [{"name": "Player 1", "guesses": 5, "max_guesses": 5, "used_letters": set(), "is_turn": True},
               {"name": "Player 2", "guesses": 5, "max_guesses": 5, "used_letters": set(), "is_turn": False}]
    
    phrases = [
        "computerscience", "doublebackflip", "boxingring", "flyingsquirrel", "highspeedchase",
        "billionaireclub", "dinosaurfossil", "spacestation", "skydivingadventure", "deepseadiving",
        "rockclimbing", "magiccarpet", "underwatervolcano", "timemachine", "mysteryisland",
        "virtualreality", "superherosquad", "rollercoaster", "hiddentreasure", "secretagent",
        "moonlanding", "spaceshuttle", "wildwest", "fastcarrace", "hightechrobot",
        "supermoon", "ancientruins", "mountainclimbing", "starshiptroopers", "parachutejump",
        "mountaincabin", "abandonedmansion", "northernlights", "tropicalrainforest"
    ]
    
    word_to_guess = random.choice(phrases) 
    revealed_word = ["_" if l != " " else " " for l in word_to_guess] 

    current_player_index = 0  
    game_over = False

    while not game_over:
        player = players[current_player_index]
        
        if player["guesses"] == 0:
            other_player = players[1 - current_player_index]  
            screen.fill(WHITE)
            draw_text(screen, f"{other_player['name']} wins!", SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3, GREEN)
            pygame.display.flip()
            wait_for_click_or_timeout(3)
            break  

        
        while "_" in revealed_word and player["guesses"] > 0:
            screen.fill(WHITE)
            draw_text(screen, f"{player['name']} - Word to guess: {' '.join(revealed_word)}", 50, 150)
            draw_text(screen, f"Guesses left: {player['guesses']}", 50, 200)
            pygame.display.flip()
            wait_for_click_or_timeout(5)

            wheel_result = spin_wheel()
            if wheel_result == "skip":
                draw_text(screen, "Turn skipped!", 50, 200)
                pygame.display.flip()
                wait_for_click_or_timeout(2)
                break 

            if wheel_result == "free_guess":
                draw_text(screen, "Free guess!", 50, 200)
                pygame.display.flip()
                wait_for_click_or_timeout(2)

                player_input = get_free_guess_input(revealed_word)
                player_input = player_input.lower()

                if player_input == word_to_guess:
                    revealed_word = list(word_to_guess)
                    draw_text(screen, "Correct! You guessed the phrase.", 50, 450)
                else:
                    player["guesses"] -= 1
                    draw_text(screen, "Incorrect. Try again next time.", 50, 450)
                pygame.display.flip()
                wait_for_click_or_timeout(3) 

            if "_" not in revealed_word:
                draw_text(screen, f"{player['name']} guessed the word!", 50, 250)
                pygame.display.flip()
                wait_for_click_or_timeout(3)
                break 

            if player["guesses"] <= 0:
                draw_text(screen, f"{player['name']} ran out of guesses!", 50, 250)
                pygame.display.flip()
                wait_for_click_or_timeout(3)
                break 

            letter_type = "consonant" if random.random() < (1/3) else "vowel"
            selected_letter = select_letter(player["used_letters"], letter_type, revealed_word).lower()
            if selected_letter in word_to_guess:
                for i, char in enumerate(word_to_guess):
                    if char == selected_letter:
                        revealed_word[i] = selected_letter
                draw_text(screen, f"Correct! {selected_letter} is in the word.", 50, 450)
            else:
                player["guesses"] -= 1
                draw_text(screen, f"Incorrect! {selected_letter} is not in the word.", 50, 450)

            player["used_letters"].add(selected_letter)
            pygame.display.flip()
            wait_for_click_or_timeout(3)

        current_player_index = (current_player_index + 1) % len(players)
    
    pygame.quit()

if __name__ == "__main__":
    main()

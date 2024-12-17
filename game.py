import random

class Game:
    def __init__(self):
        self.contestants = []
        self.used_vowels = set()
        self.prizes = []
        self.current_phase = "contestant_row"

    def play_contestant_row(self):
        print("Contestants are bidding for a chance to play!")
        self.current_phase = "mini_game"

    def play_mini_game(self):
        print("Playing a mini-game!")
        self.current_phase = "showcase_showdown"

    def play_showcase_showdown(self):
        print("It's time for the Showcase Showdown!")
        self.current_phase = "final_showcase"

    def play_final_showcase(self):
        print("Final Showcase time!")
        self.current_phase = "end_game"

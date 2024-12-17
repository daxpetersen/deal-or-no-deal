import random
from config import VOWELS

class Contestant:
    def __init__(self, name):
        self.name = name
        self.bidding = None

    def make_bid(self, bid):
        self.bidding = bid

class Prize:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class GameLogic:
    def __init__(self):
        self.contestants = []
        self.prizes = []
        self.used_vowels = set()

    def add_contestant(self, contestant):
        self.contestants.append(contestant)

    def start_contestant_row(self):
        print("Contestant Row phase starts now!")
        # Simulate contestant bidding
        for contestant in self.contestants:
            contestant.make_bid(random.randint(100, 1000))
            print(f"{contestant.name} bids {contestant.bidding}")

    def determine_winner_contestant_row(self):
        closest_bid = float('inf')
        winner = None
        for contestant in self.contestants:
            if 0 < contestant.bidding < closest_bid:
                closest_bid = contestant.bidding
                winner = contestant
        return winner

    def add_prize(self, prize):
        self.prizes.append(prize)

    def mini_game(self):
        print("Playing a mini-game!")
        prize = random.choice(self.prizes)
        print(f"Contestant wins the prize: {prize.name} worth ${prize.price}")

    def showcase_showdown(self):
        print("Spinning the Showcase Showdown wheel!")
        spin_result = random.choice(['$1', '$0.25', '$0.50', '$0.75'])
        print(f"The wheel lands on {spin_result}!")

    def select_vowel(self):
        available_vowels = [v for v in VOWELS if v not in self.used_vowels]
        selected_vowel = random.choice(available_vowels)
        self.used_vowels.add(selected_vowel)
        return selected_vowel

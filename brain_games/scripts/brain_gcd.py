from brain_games.engine import start_game
from brain_games.games.gcd import DESCRIPTION, gcd

def main():
	start_game(DESCRIPTION, gcd)
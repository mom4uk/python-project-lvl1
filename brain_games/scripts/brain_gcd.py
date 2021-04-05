# -*- coding: utf-8 -*-

"""Brain gcd game."""

from brain_games.engine import start_game
from brain_games.games.gcd import DESCRIPTION, gcd


def main():
    """Start gcd game."""
    start_game(DESCRIPTION, gcd)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

"""Brain prime game."""

from brain_games.engine import start_game
from brain_games.games.prime import DESCRIPTION, prime


def main():
    """Start prime game."""
    start_game(DESCRIPTION, prime)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

"""Brain even game."""

from brain_games.engine import start_game
from brain_games.games.even import DESCRIPTION, even


def main():
    """Start even game."""
    start_game(DESCRIPTION, even)


if __name__ == '__main__':
    main()

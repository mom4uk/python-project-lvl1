# -*- coding: utf-8 -*-

"""Brain calc game."""

from brain_games.engine import start_game
from brain_games.games.calc import DESCRIPTION, calc


def main():
    """Start calc game."""
    start_game(DESCRIPTION, calc)


if __name__ == '__main__':
    main()

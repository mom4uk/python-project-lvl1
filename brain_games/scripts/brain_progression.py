# -*- coding: utf-8 -*-

"""Brain progression game."""

from brain_games.engine import start_game
from brain_games.games.progression import DESCRIPTION, progression


def main():
    """Start progression game."""
    start_game(DESCRIPTION, progression)


if __name__ == '__main__':
    main()

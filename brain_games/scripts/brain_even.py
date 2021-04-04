#!/usr/bin/env python
from brain_games.games.even import DESCRIPTION, even
from brain_games.engine import start_game

def main():
	start_game(DESCRIPTION, even)

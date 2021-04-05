# -*- coding: utf-8 -*-

"""Brain progression game functions."""

from random import choice

from brain_games.utils import get_random_number

LENGTH_ARITHMETIC_PROGRESSION = 10
DESCRIPTION = 'What number is missing in the progression?'


def get_progression(initial_value, progression_difference, length_progression):
    """Generate progression."""
    max_value = (progression_difference * length_progression) + initial_value
    progression = range(initial_value, max_value, progression_difference)
    secret = choice(progression)
    progression_with_secret = ' '.join(
        ['..' if num == secret else str(num) for num in progression])
    stringify_progression = f'{progression_with_secret}'
    return (stringify_progression, str(secret))


def progression():
    """Generate question and correct answer."""
    progression_member = get_random_number(0, 100)
    progression_difference = get_random_number(1, 25)
    return get_progression(
        progression_member,
        progression_difference,
        LENGTH_ARITHMETIC_PROGRESSION)

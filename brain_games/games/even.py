# -*- coding: utf-8 -*-

"""Brain even game functions."""

from brain_games.utils import get_random_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """Check value is even."""
    return num % 2 == 0


def even():
    """Generate question and correct answer."""
    random_value = get_random_number(0, 100)
    correct_answer = 'yes' if is_even(random_value) else 'no'
    return (random_value, correct_answer)

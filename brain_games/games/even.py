# -*- coding: utf-8 -*-

"""Brain even game functions."""

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """Check value is even."""
    return num % 2 == 0


def even():
    """Generate question and correct answer."""
    random_value = randint(0, 100)
    correct_answer = 'yes' if is_even(random_value) else 'no'
    return (random_value, correct_answer)

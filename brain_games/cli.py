# -*- coding: utf-8 -*-

"""Welcome."""

import prompt


def welcome_user():
    """Welcome user."""
    name = prompt.string('May I have your name?')
    greeting = 'Hello, {}'
    print(greeting.format(name))

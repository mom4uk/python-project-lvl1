# -*- coding: utf-8 -*-

"""Engine module."""

import prompt


def engine(descripsion, get_task_and_answer):
    """Engine."""
    print('Welcome to the Brain Games!')
    cycles_count = 3
    name = prompt.string('May I have your name? ')
    message = "'{wrong}' is wrong answer ;(. Correct answer was '{correct}'."
    print(f'Hello, {name}')
    print(descripsion)
    while cycles_count > 0:
        (question, correct_answer) = get_task_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(message.format(wrong=answer, correct=correct_answer))
            return
        else:
            print('Correct!')
        cycles_count -= 1
    print(f'Congratulations, {name}!')


def start_game(descripsion=None, get_task_and_answer=None):
    """Start game."""
    if descripsion:
        engine(descripsion, get_task_and_answer)

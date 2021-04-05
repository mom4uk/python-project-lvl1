from brain_games.utils import get_random_number
from random import choice

LENGTH_ARITHMETIC_PROGRESSION = 10
DESCRIPTION = 'What number is missing in the progression?'


def get_progression(initial_value, progression_difference, length_progression):
    maximum_value = (progression_difference *
                     length_progression) + initial_value
    progression = range(initial_value, maximum_value, progression_difference)
    print(progression)
    secret = choice(progression)
    progression_with_secret = ' '.join(
        ['..' if value == secret else str(value) for value in progression])
    result = f"{progression_with_secret}"
    return (result, str(secret))


def progression():
    progression_member = get_random_number(0, 100)
    progression_difference = get_random_number(1, 25)
    (question, correct_answer) = get_progression(progression_member,
                                                 progression_difference, LENGTH_ARITHMETIC_PROGRESSION)
    return (question, correct_answer)

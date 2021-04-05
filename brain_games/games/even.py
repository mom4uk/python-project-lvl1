from brain_games.utils import get_random_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_Even(value):
	return value % 2 == 0

def even():
	randomValue = get_random_number()
	correctAnswer = 'yes' if is_Even(randomValue) == True else 'no'
	return (randomValue, correctAnswer)

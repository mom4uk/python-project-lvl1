import prompt


def engine(descripsion, get_task_and_answer):
    print('Welcome to the Brain Games!')
    cyclesCount = 3
    name = prompt.string('May I have your name? ')
    print("Hello, %s" % (name))
    print(descripsion)
    while cyclesCount > 0:
        (question, correct_answer) = get_task_and_answer()
        print("Question: %s" % (question))
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(
                "%s is wrong answer ;(. Correct answer was %s \nLet's try again, %s" %
                (answer, correct_answer, name))
            return
        else:
            print('Correct!')
        cyclesCount -= 1
    print("Congratulations, %s" % (name))
    return


def start_game(descripsion=None, get_task_and_answer=None):
    if descripsion:
        engine(descripsion, get_task_and_answer)

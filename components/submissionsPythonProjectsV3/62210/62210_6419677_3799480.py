score = 0
print('Welcome to Flashcards!\nAdd your own questions and answers to quiz yourself!')
user = input('Type START to begin adding flashcards: ')
if user == str.casefold('START'):
    questions = input('\nType your questions seperated by "-".\nFor example, a list of questions should look like this ↓↓\nWhat is your name?-What is your age?-What is the date?\n\nType your questions: ')
    answers = input('\nType your answers sperated by "-" in the same order as the questions\nDo not include any extra spaces, beware of upper/lowercase letters\nFor example, a list of answers should look like this ↓↓\nanswer1-answer2-answer3\n\nType your answers: ')
    list_questions = questions.split('-')
    list_answers = answers.split('-')
else:
    print('Invalid input, Goodbye.')
if user == str.casefold('START'):
    num_of_q = len(list_questions)
    while len(list_questions) != 0:
        if str.casefold(input(list_questions[0]+': ')) == str.casefold(list_answers[0]):
            print('Correct! :)')
            score = score + 1
        else:
            print('Incorrect :(\nThe correct answer was', list_answers[0])
        del list_questions[0]
        del list_answers[0]
    print('You got', score,"/", num_of_q, "correct!")
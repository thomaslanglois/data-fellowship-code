from datetime import datetime

if __name__ == "__main__":
    questions = ['What is your name?', 'How old are you?', 'What is your favourite colour']

    for i, q in enumerate(questions):
        extra = None
        answer = input('{} '.format(q))

        if i == 0:
            if len(answer) < 5:
                comment = 'Wow your name is short!'
            elif 5 <= len(answer) <= 8:
                comment = 'I like your name, it is well balanced'
            else:
                comment = 'Wow your name is long!'
        elif i == 1:
            extra = datetime.now().year - int(answer)
            if int(answer) < 21:
                comment = 'You are not allowed to drink wine.\nYou were born in {}.'.format(extra)
            else:
                comment = 'You are allowed to drink wine.\nYou were born in {}.'.format(extra)
        elif i == 2:
            if answer.lower() in ['green', 'blue', 'yellow']:
                comment = 'I like this color'
            else:
                comment = 'I do not like this color.'

        print('{}\n'.format(comment))

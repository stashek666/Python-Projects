import random


def one_day():

    exceptions = ['KillError', 'DrunkError', 'CarCrashError',
                  'GluttonyError', 'DepressionError']
    karma = 0
    count = 0

    with open('karma.log', 'w') as file:
        while karma < 500:
            count += 1
            karma += random.randint(1, 7)
            number = random.randint(1, 10)
            if number == 10:
                file.write(random.choice(exceptions) + '\n')

    print('Прошло дней: ', count)


one_day()


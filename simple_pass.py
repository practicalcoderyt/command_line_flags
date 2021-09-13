import sys
import random
import datetime

def main():
    options = {'log': False}
    read_in_command_line_options(options)
    sysargs = clean_args()
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    generated_password = ''

    try:
        amount_of_characters = int(sysargs[1])
        if amount_of_characters < 1:
            print('Error on input: ' + str(amount_of_characters))
            print('Number of characters should be a positive integer.')
            exit(1)

        for _ in range(amount_of_characters):
            generated_password += characters[random.randrange(len(characters))]

        print(generated_password)

        if options['log']:
            with open('log_file.txt', 'a+') as file:
                file.write(str(datetime.datetime.now()) + '\t' + generated_password + '\n')

    except ValueError as e:
        print(e.args[0])
        print('Number of characters should be a positive integer.')
        sys.exit(1)

def read_in_command_line_options(options):
    if '-l' in sys.argv or '--log' in sys.argv:
        options['log'] = True

def clean_args():
    args = []
    for arg in sys.argv:
        if arg[0] != '-':
            args.append(arg)
    return args

if __name__ == '__main__':
    main()
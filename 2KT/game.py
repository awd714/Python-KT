import random

WORD_FILE = 'words.txt'
GALLOWS_FOLDER = 'gallows/'
MAX_MISTAKES = 6
HIDDEN_SYMBOL = '■'


def get_word():
    file = open(WORD_FILE, 'r', encoding='utf-8')

    words = []

    for line in file:
        if line.strip() != '':
            words.append(line.strip())

    file.close()

    word_data = random.choice(words).split('|')

    return word_data[0], word_data[1]


def create_table(word):
    table = [HIDDEN_SYMBOL] * len(word)
    return table


def get_mistakes():
    return 0


def prompt():
    answer = input('Введите букву или слово целиком: ')
    return answer.strip().lower()


def show_start_message():
    print('Игра "Виселица на поле чудес"')
    print('Попробуйте угадать загаданное слово!')


def show_hint(description):
    print('Подсказка:', description)


def show_table(table):
    print(' '.join(table))


def is_word_correct(word, answer):
    return word == answer


def is_letter_correct(word, answer):
    return len(answer) == 1 and answer in word


def open_letter(word, table, letter):
    for i in range(len(word)):
        if word[i] == letter:
            table[i] = letter

    return table


def is_word_guessed(table):
    return HIDDEN_SYMBOL not in table


def is_alive(mistakes):
    return mistakes < MAX_MISTAKES


def add_mistake(mistakes):
    return mistakes + 1


def show_gallows(mistakes):
    file_name = GALLOWS_FOLDER + str(mistakes) + '.txt'

    file = open(file_name, 'r', encoding='utf-8')

    for line in file:
        print(line, end='')

    file.close()
    print()


def show_win():
    print('Поздравляем! Вы выиграли!')


def show_lose(word):
    print('Вы проиграли!')
    print('Загаданное слово:', word)

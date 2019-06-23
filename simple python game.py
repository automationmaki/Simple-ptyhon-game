import random

MAX_ERRORS = 8

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет',
              'библиотека', 'шайба', 'олимпиада')


def print_list(arg):
    print(''.join(users_word))


secret_word = random.choice(words_list)
print(secret_word)

users_word = ['*'] * len(secret_word)
print_list(users_word)


errors_counter = 0


while True:
    letter = input('введите букву:').lower()

    if len(letter) != 1 or not letter.isalpha():
        continue

    if letter in secret_word:
        for idx, char in enumerate(secret_word):
            if char == letter:
                users_word[idx] = letter

        if '*' not in users_word:
            print(f'Вы выйграли !!! слово: {secret_word}')
            break
    else:
        errors_counter += 1

        print(f'буквы {letter} нет, допущено ошибок: , {errors_counter}')
        if errors_counter == MAX_ERRORS:
            print('Игра завершена')
            break

    print_list(users_word)

print('До встречи!')

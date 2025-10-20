def is_very_long(password):
    result = len(password) > 12
    return result


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isdigit()
               and not letter.isalpha() for letter in password)


def main():

    password = input('Введите пароль: ',)
    score = 0

    scores_password = [
        is_very_long(password),
        has_digit(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password)
     ]

    for score_password in scores_password:
        if score_password:
            score += 2
    print('Рейтинг = ', score)


if __name__ == '__main__':

    main()

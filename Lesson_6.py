password = input('Введите пароль: ',)

score = 0


def is_very_long(password):
    if len(password) > 12:
        return True
    return False


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    if password.find('#') != -1 or password.find('%') != -1:
        return True
    return False


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

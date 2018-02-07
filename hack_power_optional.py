def hack_calculator(hack, letters, phrases):
    result = 0
    multiply = {}  # słownik do zapisywania ilości wystąpień litery w hack

    for letter in hack:
        if letter not in multiply:
            multiply[letter] = 1
        else:
            multiply[letter] += 1
        result += letters[letter] * multiply[letter]

    phrases_sorted = sorted(phrases, reverse=True)  # posortowane 'bonusy' wg wartości malejąco
    for phrase in phrases_sorted:
        if phrase in hack:
            result += phrases[phrase]
            hack = hack.replace(phrase, '')  # wycinam bonusy, które już wystąpiły

    return result


print(hack_calculator('aabacabaaaca',
                      letters={'a': 1, 'b': 2, 'c': 3},
                      phrases={'ba': 10, 'baa': 20}))   # 81

print(hack_calculator('advantage',
                      letters={'a': 1, 'd': 2, 'e': 5, 'g': 2, 'n': 1, 't': 4, 'v': 7},
                      phrases={'ad': 10, 'ant': 13, 'age': 24, 'van': 13, 'tag': 5}))   # 55

print(hack_calculator('aaaaa',
                      letters={'a': 1},
                      phrases={'a': 1000,
                               'aa': 2000,
                               'aaa': 3000,
                               'aaaa': 4000}))  # 5015

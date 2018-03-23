def hack_calculator(hack, letters, phrases):
    result = 0
    multiply = {}  # słownik do zapisywania ilości wystąpień litery w hack
    try:
        for letter in hack:
            multiply.setdefault(letter, 0)
            if letter in multiply:
                multiply[letter] += 1
            result += letters[letter] * multiply[letter]

        phrases_sorted = sorted(phrases, reverse=True)  # posortowane 'bonusy' wg wartości malejąco
        for phrase in phrases_sorted:
            if phrase in hack:
                result += phrases[phrase] * hack.count(phrase)
                hack = hack.replace(phrase, '')  # wycinam bonusy, które już wystąpiły

        return result
    except KeyError:
        return 0


print(hack_calculator('advantage',
                      letters={'a': 1, 'd': 2, 'e': 5, 'g': 2, 'n': 1, 't': 4, 'v': 7},
                      phrases={'ad': 10, 'ant': 13, 'age': 24, 'van': 13, 'tag': 5}))   # 55

print(hack_calculator('baaca', letters={'a': 1, 'b': 2, 'c': 3}, phrases= {'ba': 10, 'baa':20}))  # 31
print(hack_calculator('babacaba', letters={'a': 1, 'b': 2, 'c': 3}, phrases= {'ba': 10, 'baa':20}))  # 55
print(hack_calculator('aabacabaaaca', letters={'a': 1, 'b': 2, 'c': 3}, phrases= {'ba': 10, 'baa':20}))  # 81
print(hack_calculator('abc', letters={'a': 1, 'b': 2, 'c': 3}, phrases= {'ba': 10, 'baa':20}))  # 6
print(hack_calculator('baad', letters={'a': 1, 'b': 2, 'c': 3}, phrases= {'ba': 10, 'baa':20})) # 0

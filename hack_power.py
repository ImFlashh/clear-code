powers = {'a': 1,
          'b': 2,
          'c': 3}


def hack_calculator(hack):
    try:
        result = 0
        multiply = {'a': 0, 'b': 0, 'c': 0}  # słownik do zliczania ilości wystąpień liter
        for element in hack:
            multiply[element] += 1
            if element in powers:
                result += powers[element] * multiply[element]

        if 'baa' in hack:
            result += (hack.count('baa') * 20)  # wycinam bonusy 'baa' żeby 'ba' nie bonusowało ponownie
            hack = hack.replace('baa', '')
        if 'ba' in hack:
            result += (hack.count('ba') * 10)
        return result
    except KeyError:
        return 0


print(hack_calculator('baaca'))  # 31
print(hack_calculator('babacaba'))  # 55
print(hack_calculator('aabacabaaaca'))  # 81
print(hack_calculator('abc'))  # 6
print(hack_calculator('ccbc'))  # 20
print(hack_calculator('aaad'))  # 0

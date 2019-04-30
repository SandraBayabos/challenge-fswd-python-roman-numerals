# ROMAN NUMERALS

num = int(input('Enter a number: '))

roman_numbers = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
matching_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def romanize(number):
    roman = ""
    for index, num in enumerate(matching_numbers):
        while number >= num:
            number = number - num
            roman = roman + roman_numbers[index]
    return roman


print(romanize(num))

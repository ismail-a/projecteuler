#!/usr/bin/env python3
# __author__ = 'ismail'


def num2word(num):
    numWords = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
                30: 'thirty', 40: 'forty', 50: 'fifty',
                60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
                100: 'one hundred', 1000: 'one thousand'}
    if 1 <= num <= 20 or num == 100 or num == 1000:
        return numWords[num]
    if 20 < num < 100:
        word = numWords[num - num % 10]
        if num % 10 is not 0:
            word += '-' + numWords[num % 10]
        return word
    if 100 < num < 1000:
        word = numWords[num // 100] + ' '
        if num > 100:
            word += 'hundred'
        if num % 100 is not 0:
            word += ' and '
            word += str(num2word(num % 100))
        return word


def lengthOfNumWord(num):
    word = num2word(num)
    # print(word)
    return len(word.replace('-', '').replace(' ', ''))

length = 0
n = 1000

for i in range(1, n + 1):
    length += lengthOfNumWord(i)

print(length)
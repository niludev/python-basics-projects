""" import digitFinder
digitFinder.digit_finder(512) """

from digitFinder import digit_finder

def has_condition(num):
    digits = set()
    
    while num > 0:
        foundedDigit = num % 10
        digits.add(foundedDigit)
        """ num //= 10 """
        num = num // 10
        """ print(foundedDigit) """

    """ print(digits) """
    
    return not (digits.__contains__ (0) or digits.__len__() != 2)

def main():
    count = 0
    for num in range(100, 999):
        if has_condition(num):
            count += 1
            """ print(num) """
    print(count)    

main()
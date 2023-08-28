def digit_finder (num):
    digits =[]

    while num > 0:
        foundedDigit = num % 10
        digits.append(foundedDigit)
        num = num // 10

    digits.reverse()
    print(digits)
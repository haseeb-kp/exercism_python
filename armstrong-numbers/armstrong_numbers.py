def is_armstrong_number(number):
    length = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10
    return number == sum


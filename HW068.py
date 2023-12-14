from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):

    getcontext().prec = signs_count
    decimal_number = [Decimal(num) for num in number_list]
    total = sum(decimal_number)
    average = total / len(decimal_number)
    return Decimal(average)

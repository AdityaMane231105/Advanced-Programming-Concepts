def decimal_to_binary(number):
    if number < 0:
        return "-" + decimal_to_binary(-number)
    if number < 2:
        return str(number)
    return decimal_to_binary(number // 2) + str(number % 2)


print(decimal_to_binary(25))

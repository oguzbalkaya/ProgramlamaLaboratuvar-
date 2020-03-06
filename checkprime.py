def check_prime(number):
    if number!=1:
        for factor in range(2,number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

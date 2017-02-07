def is_prime(number):
    for number in range(1, 50):
        if number <= 1:
            return False
        for x in range(2, number):
            if number % x == 0:
                return False

    return True

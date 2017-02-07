def fizz_buzz(arg):
    if arg % 3 == 0:
        if arg % 5 == 0:
            return "FizzBuzz"
        return "Fizz"
    elif arg % 5 == 0:
        return "Buzz"
    return arg

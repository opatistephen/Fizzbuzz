def fizzbuz():
    checkNum=3

    if checkNum%5==0 and checkNum%3==0:
        print("FizzBuz")
    elif checkNum%5==0:
        print("Buzz")
    elif checkNum%3==0:
        print("Fizz")
    else:
        print("checkNum")

fizzbuz()
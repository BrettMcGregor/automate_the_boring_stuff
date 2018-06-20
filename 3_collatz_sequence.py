#Collatz sequence using a loop


def collatz(number):
    if number % 2 == 0:
        return number // 2
    return 3 * number + 1


def collatz_sequence():
    try:
        raw_input = int(input("Please enter an integer: "))
        s = raw_input
        while s > 1:
            print(s)
            s = collatz(s)
    except ValueError:
        print("Non integer entered.\n")
        collatz_sequence()
    return 1


# print(collatz_sequence())


# Collatz sequence using a generator function


def collatz_generator(s):
    while s > 1:
        yield s
        s = collatz(s)  # utilising the collatz() function to perform the required computation for generator
    yield 1


while True:
    try:
        for i in collatz_generator(int(input("Please enter an integer > "))):
            print(i)
    except ValueError:
        print("You did not enter an integer! Try again.")

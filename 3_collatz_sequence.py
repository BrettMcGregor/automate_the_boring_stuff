def collatz(number):
    if number % 2 == 0:
        return number // 2
    return 3 * number + 1


def collatz_sequence(number):
    while number != 1:
        print(collatz(number))


print(collatz_sequence(int(input("Please enter an integer: "))))

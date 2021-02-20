# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.

# Fizz buzz game - 2nd iteration (testable)

def fizz_buzz_game(i):
    '''
    analyses the input i and determines if i should be called tests, fizz or buzz
    :param i: integer
    :return: string tests when divisible by 3 and 5; fizz when divisible by 3 and buzz when divisible by 5.
    '''
    if i % 15 == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        return i


def main():
    for i in range(1, 101):
        print(fizz_buzz_game(i))


# Press the green button in the gutter to run the script.
# this is a top level script environment (https://docs.python.org/3/library/__main__.html)
# this function executes automatically ehrn the script is run directly but not when imported by another script.
if __name__ == '__main__':
    main()

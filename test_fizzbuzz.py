import unittest

from fizzbuzz_2nditer import fizz_buzz_game


class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        '''
        covers tests that are divisible by 3 and return 'fizz'
        :return: string fizz
        '''
        for i in [3, 6, 9, 12, 18]:
            print('testing', i)
            assert fizz_buzz_game(i) == "fizz"

    def test_buzz(self):
        '''
        test cases that are divisible by 5 and return 'buzz'
        :return: string buzz
        '''
        for i in [5, 10, 50]:
            print('testing', i)
            assert fizz_buzz_game(i) == "buzz"

    def test_fizzbuzz(self):
        '''
        covers test cases which are divisable by both 3 AND 5 and return 'fizzbuzz'
        :return: string fizzbuzz
        '''
        for i in [15, 30, 45, 75]:
            print('testing', i)
            assert fizz_buzz_game(i) == "fizzbuzz"

    def test_number(self):
        '''
        covers cases which are NOT divisible by 3 or 5
        :return: int number
        '''
        for i in [2, 4, 88]:
            print('testing', i)
            assert fizz_buzz_game(i) == i


if __name__ == '__main__':
    unittest.main()

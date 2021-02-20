# Unit tests in Python 🗒️
Or _How to write unit tests in Python_ (inspired by Miguel Grinberg's [blogpost](https://blog.miguelgrinberg.com/post/how-to-write-unit-tests-in-python-part-1-fizz-buzz)) ⚗️

> This repository contains notes and programs used to used Unit Tests in Python.
## Part 1 - Intro

### Why test your code?

### Why automate tests?

### Types of tests
#### Unit testing
Involves evaluating individual components of a project to assure they behave as expected.

#### Integration testing
Involves evaluating two or more components of a project to make sure they work as a group - i.e., that they integrate well.

![img.png](https://i.stack.imgur.com/yHGn1.gif)


#### Functional testing
Requires the evaluation of features or functions of a project end-to-end to make sure it works as planned.

**Role of Thumb**: Test as much code as possible with unit tests, since they are easier to write and to run.

A test does two things:
1. runs a small part of the application
2. verifies (i.e., _asserts_) that resulting output of the code is correct

### Execution
To execute such tests, one should save the test function as a Python file and start a _test runner_, that will find and 
alert any failed assertions.

### Frameworks
Miguel uses a hybrid of both packages on his testing solutions so that is what will be seen here.
+ `unittest` package
    - will be used to structure and organise the tests on a OOP-approach based on the `TestCase`.
+ `pytest` package
    - enhanced `assert` function that provides more verbose failure outputs
    - choice of test runner since fully supports the `TestCase` class from `unittests`. 
    
### Test a full app
To explain the theory, we will code the [Fizz Buzz game](https://en.wikipedia.org/wiki/Fizz_buzz)

Check out the unfactored original code [here](../fizzbuzz_1stiter.py). And the testable and factored commented version in
[here](../fizzbuzz_2nditer.py).

To run a test simply type
```shell
pytest
```
on terminal with the test.py file on the same folder as the function to be tested.

A auccessful test will look like this:
```shell
(fizz-buzz_env) lais@lais-xps:~/Documents/projects/fizzbuzz_unit-test$ pytest
==================================================================================================== test session starts =====================================================================================================
platform linux -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /home/lais/Documents/projects/fizzbuzz_unit-test
collected 1 item                                                                                                                                                                                                             

test_fizzbuzz.py .                                                                                                                                                                                                     [100%]

===================================================================================================== 1 passed in 0.04s ======================================================================================================
```

On the other hand, a failing test will look like this:
```shell
========================================================================================================== FAILURES ==========================================================================================================
___________________________________________________________________________________________________ TestFizzBuzz.test_fizz ___________________________________________________________________________________________________

self = <test_fizzbuzz.TestFizzBuzz testMethod=test_fizz>

    def test_fizz(self):
        for i in [3, 4, 6, 9, 18]:
            print('testing', i)
>           assert fizz_buzz_game(i) == "fizz"
E           AssertionError: assert 4 == 'fizz'
E            +  where 4 = fizz_buzz_game(4)

test_fizzbuzz.py:10: AssertionError
---------------------------------------------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------------------------------------------
testing 3
testing 4
================================================================================================== short test summary info ===================================================================================================
FAILED test_fizzbuzz.py::TestFizzBuzz::test_fizz - AssertionError: assert 4 == 'fizz'
===================================================================================================== 1 failed in 0.05s ======================================================================================================
```

## Add `pytest coverage` to `pytest`
- Install the library with
```shell
conda install -c conda-forge pytest-cov
```
- Run `pytest --cov=fizzbuzz_2nditer` to show the percentage of coverage on your tests.
- Run `pytest --cov=fizzbuzz_2nditer --cov-report=term-missing` to add the number of the lines of code that were not covered.
- Run `pytest --cov=fizzbuzz_2nditer --cov-report=term-missing --cov-branch` treats lines with conditionals (`if`) as 
  needed double coverage to account for the two possible outcomes (truthy and falsey evals), named _branch coverage_.
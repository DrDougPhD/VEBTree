from VEB import VEB
import random
import time


DEFAULT_TEST_SIZE = 50000


def test_correctness(n=DEFAULT_TEST_SIZE):
    print('Creating VEB Tree for {} elements'.format(n))
    veb = VEB(n)

    print('Testing')
    
    print('Generating random numbers to sample')
    numbers = set()
    for i in range(n): 
        number = random.randint(0, veb.u-1)
        numbers.add(number)
    
    # Non-member numbers
    non_member_numbers = set()
    for i in range(n):
        non_member_numbers.add(random.randint(0, veb.u-1))
    
    print('Adding numbers to VEB Tree')
    # TODO: Implement an insert_all function
    for num in numbers:
        veb.insert(num)
    
    print('Testing for membership of numbers')
    # test for membership
    non_member_numbers = non_member_numbers - numbers
    error = 0
    for num in list(non_member_numbers):
        if veb.member(num):
            error += 1
    for num in numbers:
        if not veb.member(num):
            error += 1
    print('Error Number For Membership was {}'.format(error))

    print('Testing for successor')
    # test for successor
    sorted_numbers = sorted(numbers)
    error = 0
    for index in range(len(sorted_numbers) - 1):
        if veb.successor(sorted_numbers[index]) != sorted_numbers[index+1]:
            error += 1
    print('Error Number For successor was {}'.format(error))

    print('Testing for predecessor')
    # test for predecessor
    error = 0
    for index in range(1, len(sorted_numbers)):
        if veb.predecessor(sorted_numbers[index]) != sorted_numbers[index-1]:
            error += 1
    print('Error Number for predecessor was {}'.format(error))


def test_speed(n=DEFAULT_TEST_SIZE):
    veb = VEB(n)

    print('Creating VEB Tree for {} elements'.format(n))

    # create random numbers
    numbers = set()
    for i in range(n): 
        number = random.randint(0, veb.u-1)
        numbers.add(number)

    with Timer(message='Speed per insertion') as t:
        for number in numbers:
            veb.insert(number)

    with Timer(message='Speed per membership query') as t:
        for number in numbers:
            veb.member(number)

    with Timer(message='Speed per predecessor query') as t:
        for number in numbers:
            veb.predecessor(number)

    with Timer(message='Speed per successor query') as t:
        for number in numbers:
            veb.successor(number)

"""
Source: http://preshing.com/20110924/timing-your-code-using-pythons-with-statement/
"""
class Timer(object):
    def __init__(self, message=None):
        self.message = message

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

        if self.message:
            print('{0.message}: {0.interval} seconds'.format(self))


test_correctness(n=500)
test_speed(n=500)
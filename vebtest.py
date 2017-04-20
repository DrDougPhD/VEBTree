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
    for num in list(numbers):
        veb.insert(num)
    
    print('Testing for membership of numbers')
    # test for membership
    non_member_numbers = non_member_numbers - numbers
    error = 0
    for num in list(non_member_numbers):
        if veb.member(num):
            error += 1
    for num in list(numbers):
        if not veb.member(num):
            error += 1
    print('Error Number For Membership was {}'.format(error))

    print('Testing for successor')
    # test for successor
    listofnums = list(numbers)
    listofnums.sort()
    error = 0
    for index in range(len(listofnums) - 1):
        if veb.successor(listofnums[index]) != listofnums[index+1]:
            error += 1
    print('Error Number For successor was {}'.format(error))

    print('Testing for predecessor')
    # test for predecessor
    error = 0
    for index in range(1, len(listofnums)):
        if veb.predecessor(listofnums[index]) != listofnums[index-1]:
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
    
    total_time = 0
    starttime = time.time()
    for number in numbers:
        veb.insert(number)
    total_time = (time.time() - starttime)
            
    ns = float(len(numbers))
    total_time = float(total_time)

    print('Speed per insertion: {} seconds'.format((total_time / ns)))

    total_time = 0
    starttime = time.time()
    for number in numbers:
        veb.member(number)
    total_time = (time.time() - starttime)   

    print('Speed per membership query: {} seconds'.format(
        (total_time / ns)))

    total_time = 0
    starttime = time.time()
    for number in numbers:
        veb.predecessor(number)
    total_time = (time.time() - starttime)

    print('Speed per predecessor query: {} seconds'.format((total_time / ns)))

    total_time = 0
    starttime = time.time()
    for number in numbers:
        veb.successor(number)
    total_time = (time.time() - starttime)
    
    print('Speed per successor query: {} seconds'.format((total_time / ns)))

test_correctness(n=500)
test_speed(n=500)
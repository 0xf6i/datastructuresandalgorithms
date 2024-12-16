import time

from ordered_list import OrderedList
from priority_queue import PriorityQueue

def TestsOrderedList():
    ds_name = 'OrderedList'
    print('{0} TEST'.format(ds_name))
    print('Testing {0} with ints'.format(ds_name))
    i_list = OrderedList()
    
    

    print('New {0} should be empty ....'.format(ds_name), end='')
    if not i_list.is_empty():
        print(' but was not')
        return False
    print(' OK!')
    
    


    print('Using add() with integers 30, 20, and 10....: ', end='')
    for i in range(3,0,-1):
        i_list.add(i * 10)
    print()
    
    

    result_string = ''
    control_string = '10,10 20,20 30,30 '
    print('Using first() and remove_first() on {0} until empty .....'.format(ds_name), end='')
    while not i_list.is_empty():
        result_string += str(i_list.first())
        result_string+=',' + str(i_list.remove_first()) + ' '

    if result_string != control_string:
        print('expected {0} but got {1} '.format(control_string, result_string))
        return False
    print(' OK!')
    
    

    print('Using add() with integers 10,20 and 30....: ', end='')
    for i in range(1,4):
        i_list.add(i * 10)
    print()

    result_string = ''
    control_string = '30,30 20,20 10,10 '
    print('Using last and remove_last on {0} until empty .....'.format(ds_name), end='')
    while not i_list.is_empty():
        result_string += str(i_list.last())
        result_string+=',' + str(i_list.remove_last()) + ' '

    if result_string != control_string:
        print('expected {0} but got {1}'.format(control_string, result_string))
        return False
    print(' OK!')
    
    


    print('Mixing the aforementioned functions  ......  ', end='')
    for i in range(1,3):
        i_list.add(i * 11)
    i_list.remove_first()
    for i in range(3,5):
        i_list.add(i * 11)
    for i in range(1,3):
        i_list.remove_last()
    for i in range(9,12):
        i_list.add(i * 11)
    i_list.remove_first()
    for i in range(5,8):
        i_list.add(i * 11)

    result_string = ''
    while not i_list.is_empty():
        result_string += str(i_list.remove_first()) + ' '
        result_string += str(i_list.remove_last()) + ' '
    control_string = '55 121 66 110 77 99 '
    if result_string != control_string:
        print(' expected {0} but got {1}'.format(control_string,result_string))
        return False
    print(' OK!')
    
    


    print('Using add and remove_at on prepopulated {0} .... '.format(ds_name))

    print('  Adding 0,1,2,...,7,8,9 using add()')
    for i in range(10):
        i_list.add(i)

    print('  checking size() .. ', end='')
    if i_list.size() != 10:
        print(' expected size() == 10, but is {0}'.format(i_list.size()))
        return False
    print('OK!')
    
    

    print('  Calling remove_at() for values 9, 5, 2, 0')
    i_list.remove_at(9)
    i_list.remove_at(5)
    i_list.remove_at(2)
    i_list.remove_at(0)

    print('  checking size() .. ', end='')
    if i_list.size() != 6:
        print(' expected size() == 6, but is {0}'.format(i_list.size()))
        return False
    print('OK!')
    
    

    print('  Calling add() with 0, 2, 5, and 9')
    i_list.add(0)
    i_list.add(2)
    i_list.add(5)
    i_list.add(9)

    print('  checking size() .. ', end='')
    if i_list.size() != 10:
        print(' expected size() == 10, but is {0}'.format(i_list.size()))
        return False
    print('OK!')
    
    

    print('  calling get_at() for indices 0,2,9 ...', end='')
    result_string = ""
    result_string += str(i_list.get_at(0)) + ", "
    result_string += str(i_list.get_at(2)) + ", "
    result_string += str(i_list.get_at(9))
    control_string = "0, 2, 9"
    if result_string != control_string:
        print('Expected {0} but got {1}'.format(control_string, result_string))
        return False
    print(' OK!')
    
    

    print('  Calling remove_last() until {0} is empty using is_empty() .... '.format(ds_name))
    result_string = ''
    control_string = '9 8 7 6 5 4 3 2 1 0 '
    control_string = '0 1 2 3 4 5 6 7 8 9 '
    while not i_list.is_empty():
        result_string += str(i_list.remove_first()) + ' '

    if result_string != control_string:
        print('Expected {0} but got {1}'.format(control_string, result_string))
        return False
    print('OK!')
    
    


    print()
    print('Testing {0} with strings .... '.format(ds_name))
    s_list = OrderedList()

    print('Testing add() with A, B, C and D .... ', end='')
    s_list.add('B')
    s_list.add('D')
    s_list.add('A')
    s_list.add('C')

    result_string = ''
    control_string = 'ABCD'

    while not s_list.is_empty():
        result_string += s_list.remove_first()
    if result_string != control_string:
        print(' expected {0} but got {1}'.format(control_string, result_string))
        return False

    print(' OK!')
    
    
    return True

def ExceptionsOrderedList():
    ds_name = 'OrderedList'
    print('{0} EXCEPTIONS'.format(ds_name))
    print('Testing {0} for exceptions'.format(ds_name))

    i_list = OrderedList()

    #first på empty
    print('using first() with empty {0} ... '.format(ds_name), end='')
    try:
        i_list.first()
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        
    
    #last på empty
    print('using last() with empty {0} ... '.format(ds_name), end='')
    try:
        i_list.last()
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        

    # remove_first på empty
    print('using remove_first() with empty {0} ... '.format(ds_name), end='')
    try:
        i_list.remove_first()
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        

    # remove_last på empty
    print('using remove_last() with empty {0} ... '.format(ds_name), end='')
    try:
        i_list.remove_last()
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        

    # remove at > 1
    print('using remove_at(0) on empty {0} ... '.format(ds_name), end='')
    try:
        i_list.remove_at(0)
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        

    print('using get() on empty {0} ... '.format(ds_name), end='')
    try:
        i_list.get_at(0)
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        
    return True

    i_list.add(1)
    # remove_at < 0
    print('using remove(11) for non-existing index ... ', end='')
    try:
        i_list.remove(11)
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        

    print('using remove(-1) for negative index ... ', end='')
    try:
        i_list.remove(-1)
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        

    print('using get(-1) with negative index ... ', end='')
    try:
        i_list.get_at(-1)
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        
    return True

    print('using get(1) with index out of bounds ... ', end='')
    try:
        i_list.get_at(1)
        print(' expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        
    return True


def TestsMinPriorityQueue():
    ds_name = 'PriorityQueue'
    print('{0} TEST'.format(ds_name))
    print('Testing {0} with ints'.format(ds_name))
    i_pq = PriorityQueue()

    print('New {0} should be empty ....'.format(ds_name), end='')
    if not i_pq.is_empty():
        print(' but was not')
        return False
    print(' OK!')
    
    

    print('Using insert() with integers 30, 20, and 10....: ', end='')
    for i in range(3,0,-1):
        i_pq.enqueue(i * 10)
    print()

    result_string = ''
    control_string = '10,10 20,20 30,30 '
    print('Using peek() and extract_min() on {0} until empty .....'.format(ds_name), end='')
    while not i_pq.is_empty():
        result_string += str(i_pq.peek())
        result_string+=',' + str(i_pq.dequeue()) + ' '

    if result_string != control_string:
        print('expected {0} but got {1}'.format(control_string, result_string))
        return False
    print(' OK!')
    
    


    print('Mixing the aforementioned functions  ......  ', end='')
    for i in range(1,3):
        i_pq.enqueue(i * 11)
    i_pq.dequeue()
    for i in range(3,5):
        i_pq.enqueue(i * 11)
    for i in range(1,3):
        i_pq.dequeue()
    for i in range(9,12):
        i_pq.enqueue(i * 11)
    i_pq.dequeue()
    for i in range(5,8):
        i_pq.enqueue(i * 11)

    result_string = ''
    while not i_pq.is_empty():
        result_string += str(i_pq.dequeue()) + ' '
    control_string = '55 66 77 99 110 121 '
    if result_string != control_string:
        print(' expected {0} but got {1}'.format(control_string,result_string))
        return False
    print(' OK!')
    
    


    print('Testing {0} with strings .... '.format(ds_name))
    s_list = PriorityQueue()

    print('Testing add() with A, B, C and D .... ', end='')
    s_list.enqueue('B')
    s_list.enqueue('D')
    s_list.enqueue('A')
    s_list.enqueue('C')

    result_string = ''
    control_string = 'ABCD'

    while not s_list.is_empty():
        result_string += s_list.dequeue()
    if result_string != control_string:
        print(' expected {0} but got {1}'.format(control_string, result_string))
        return False

    print(' OK!')
    print('All tests for {0} OK!'.format(ds_name))
    
    
    return True


def ExceptionsPriorityQueue():
    ds_name = 'PriorityQueue'
    print('{0} EXCEPTIONS '.format(ds_name))
    pq = PriorityQueue()

    print('calling dequeue() on empty {0} .. '.format(ds_name), end='')
    try:
        pq.dequeue()
        print('expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        

    print('calling peek() on empty {0} .. '.format(ds_name), end='')
    try:
        pq.peek()
        print('expected exception to be raised.')
        return False
    except Exception as e:
        print('OK!')
        
        

    print('All exceptions for {0} OK!'.format(ds_name))
    return True

def main():
    print('Starting funcionality tests on OrderedList...')
    if not TestsOrderedList():
        print()
        print('Functionality tests failed. See above.')
        return 1
    print()
    print('Starting exception tests on OrderedList...')
    if not ExceptionsOrderedList():
        print()
        print('Exception tests failed. See above.')
        return 1

    print()
    print('------------------')
    print('Starting funcionality tests on PriorityQueue...')

    if not TestsMinPriorityQueue():
        print()
        print('Functionality tests failed. See above.')
        return 1
    print()
    print('Starting exception tests on PriorityQueue...')
    if not ExceptionsPriorityQueue():
        print()
        print('Exception tests failed. See above.')
        return 1

    print()
    print('All tests passed!')
    print('You can now hand in your code to the instructor.')

if __name__ == '__main__':
    main()
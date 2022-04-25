def one(n): 
    '''
    Function to return the sum of all integers from 1 to n recursively
    :param n: the biggest number that is added
    '''
    check(n)
    if(n == 1):
        return n
    else: 
        return (n + one(n - 1))

def two(num, pow):
    '''
    Function to return the power of a number recursively
    :param num: the base number
    :param pow: the value of the exponent that num is being raised to
    '''
    check(num, pow)
    if(pow == 0):
        return 1
    if(pow == 1):
        return num
    else: 
        return (num * two(num, pow - 1))

def three(n):
    '''
    Funtion to print out all the numbers from an inputted value to 1 in decending order
    :param n: the starting number for the countdown
    '''
    check(n)
    if(n == 1):
        return 1
    else: 
        return(f'{n} {three(n - 1)}')


def main():
    '''
    Function to call and run the program's functions
    '''
    print(one(1))       # 1
    print(one(2))       # 3
    print(one(3))       # 6
    print(one(4))       # 10

    print()
    print(two(2, 1))    # 2
    print(two(2, 2))    # 4
    print(two(2, 3))    # 8
    print(two(3, 4))    # 81

    print()
    print(three(5))           # 5 4 3 2 1
    print()
    print(three(10))          # 10 9 8 7 6 5 4 3 2 1

def check(*args):
    '''
    Function to check if the inputted value is an integers
    :param args: allows this function to be called with varying numbers of parameters
    '''
    for i in args:
        i = str(i)
        if((i.isnumeric() == False)):
            raise TypeError('Please enter an Integer')


if __name__ == '__main__':
    main()

#BT3051 Assignment 2
#Roll Number: MM14B022
#Collaborators: BS14B003
#Time: 0:10

import doctest
def armstrong(start,end):
    """
    Giving all Armstrong numbers between a given range of numbers

    This function checks each number between given numbers and print if it is
    and Armstrong number.

    Args:
    start (int): Start of the range
    end (int): End of the range

    Returns:
    answer (str): String containing Armstrong numbers comma separated

    >>> armstrong(1,1000)
    1, 153, 370, 371, 407
    """
    answer = ''
    for num in range(start,end+1):
        string = str(num)
        if (sum([int(x)**3 for x in string]) == num):
            answer += str(num)+', '
    return print(answer.strip(', '))

print(armstrong(1,1000))

if __name__ == '__main__':
    doctest.testmod(verbose = True)

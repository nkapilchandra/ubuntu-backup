#BT3051 Assignment 2
#Roll Number: MM14B022
#Collaborators: BS14B003
#Time: 0:40


"""
In the following program I have written code which takes input from hw2b_input.txt
and outputs the result into hw2b_output.txt
"""

import doctest
def bin_to_dec(binary):
    """
    Function to convert binary numbers to decimal numbers

    Args:
    bindary (str): Binary number in string form

    Returns:
    dec (int): Decimal numbers

    >>> bin_to_dec('1100')
    12
    >>> bin_to_dec('1010')
    10
    """
    n = len(binary)
    dec = 0
    for i in range(n-1,-1,-1):
        if (binary[i] == '1'):
            dec += 2**(n-i-1)
    return dec

answer = []
with open('hw2b_input.txt','r') as f:
    data = f.readlines()
    for line in data:
        line = line.strip()
        line = line.strip(',')
        line = line.split(',')
        for i in line:
            answer += [bin_to_dec(i)]

with open('hw2b_output.txt','w') as f:
    answer.sort()
    string = ''
    for i in answer:
        string += str(i) + ','
    string = string.strip(',')
    f.write(string)

if __name__ == '__main__':
    doctest.testmod(verbose = True)

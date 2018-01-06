#BT3051 Assignment 2
#Roll Number: MM14B022
#Collaborators: BS14B003
#Time: 0:50

"""
This code takes input from hw2c_input.txt and then outputs to hw2c_output.txt
"""
import string
import doctest
def validate(password):
    """
    Validation of password

    Args:
    password (str): Password to be checked

    Returns:
    boolean : Whether or not it is a valid password

    >>> validate('@Bt3051')
    True
    >>> validate('CRC101')
    False
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punc = string.punctuation
    punc += ' '
    special = '$!@'
    n = len(password)
    for i in special:
        punc = punc.replace(i,'')
    lc,uc,dig,spc,pun = [False]*5
    for i in lowercase:
        if i in password:
            lc = True
            break
    for i in uppercase:
        if i in password:
            uc = True
            break
    for i in digits:
        if i in password:
            dig = True
            break
    for i in special:
        if i in password:
            spc = True
            break
    for i in punc:
        if i in password:
            pun = True
    if (lc and uc and dig and spc and (not pun) and (n>=4) and (n<=8)):
        return True
    else:
        return False

answer = ''
with open('hw2c_input.txt','r') as f:
    data = f.readlines()
    for line in data:
        line.strip()
        line = line.split(',')
        for i in line:
            if validate(i):
                answer += i + ','
with open('hw2c_output.txt','w') as f:
    f.write(answer.strip(','))

if __name__ == '__main__':
    doctest.testmod(verbose = True)

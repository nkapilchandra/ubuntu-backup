#BT3051 Assignment 0b
#Roll number: MM14b022
#Collaborators: None
#Time: 0:10
n = int(input('Enter a number> '))
print (n)
while (n !=1 ):
    if (n % 2 == 0):
        n =  int(n/2)
        print (n)
    else:
        n = 3*n + 1
        print (n)

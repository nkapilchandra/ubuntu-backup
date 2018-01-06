#BT3051 Assignment 2
#Roll Number: MM14B022
#Collaborators: BS14B003
#Time: 0:30

def capital(input_file):
    """
    Capitalizing first letter of words and sorting

    This functions takes a file containing words separated by commas and
    capitalizes the first letter of each word, sorts the words and then outputs
    the resulting words comma separated into the same file.

    Args:
    input_file (str): File name from which words have to be read

    """
    with open(input_file,'r') as f:
        string=''
        data = f.readlines()
        for line in data:
            line = line.strip()
            line = line.strip(',')
            line = line.split(', ')
            ans=[]
            for i in line:
                print(i)
                j = i[0].capitalize() + i[1:]
                ans += [j]
            ans.sort()
            print(ans)
            for i in ans:
                string += i+', '
    with open(input_file,'w') as g:
        string = string.strip(', ')
        g.write(string)

capital('hw2a_input.txt')

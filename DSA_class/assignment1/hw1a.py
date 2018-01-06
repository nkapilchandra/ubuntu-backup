# BT3051 Assignment 1a
# Roll number: MM14B022
# Collaborators: BS14B003
# Time: 0:45
import sys
def read_fasta(fname):
    """ (str) -> (list of tuples)
    Read a fasta foramtted file.

    Args:
    fname (str): The fasta file name

    Returns:
    content (list): List containing sequences and their names

    """
    f = open(fname,'r')
    content = []
    name = None
    string = ''
    for line in f:
        if (line[0]!= '>'):
            string += line[:-1]
        else:
            if (name != None):
                content.append((name,string))
                string = ''
            name = line[1:-1]
    content.append((name,string))
    f.close()
    return content # a list of (sequence_name, sequence) tuples

def compute_protein_mass(protein_str):
    """
    Computing the mass of the protein sequence.

    This function computes the mass of the protein sequence given based on the
    weights provided in the file PROT_MASS.txt.

    Args:
    protein_str (str): The protein sequence

    Returns:
    mass (float): Mass of the protein sequence
    
    >>> compute_protein_mass('SKADYEK')
    821.392
    >>> compute_protein_mass('KAPIL')
    522.353
    """
    f = open('PROT_MASS.txt','r')
    mass_dict = {}    #Dictionary to store weights

    #Code to read from the file and store the weights in a dictionary
    for line in f:
        mass_dict[line.split('   ')[0]] = float(line.split('   ')[-1][:-1])
    mass = 0

    #Code to compute mass
    for i in protein_str:
        mass += mass_dict[i]
    f.close()
    return round(mass,3)


if __name__ == '__main__':
    #DO NOT CHANGE THE FOLLOWING STATEMENTS
    for seq_name, seq in read_fasta("hw1a_dataset.faa"):
        print (seq_name, compute_protein_mass(seq))

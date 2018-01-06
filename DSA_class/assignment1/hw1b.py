# BT3051 Assignment 1b
# Roll number: MM14B022
# Collaborators: BS14B003
# Time: 1:15
import doctest

def translate_DNA(mrna, translation_table = 'RNA_TABLE.txt'):
    """
    Tranlating mRNA to protein

    This function takes a mRNA sequence and translates it into protein sequence
    based on the 64 kinds of encodings given in the file RNA_TABLE.txt. All the
    encodings are stored in the form of dictionary for the ease of usage.

    Args:
    mrna (str): The mRNA sequence
    translation_table (str): The file name that contains the RNA_TABLE (default 'RNA_TABLE.txt')

    Returns:
    encoding (str): The translated protein sequence

    >>> translate_DNA('AUGUAUGAUGCGACCGCGAGCACCCGCUGCACCCGCGAAAGCUGA')
    MYDATASTRCTRES
    >>> translate_DNA('AUAGCCAUGGAUGAGGUAAUACUAUAA')
    IAMDEVIL
    """
    f = open(translation_table,'r')
    rna_dict = {}     # Stores the encoding values of RNA codons
    encoding = ''     # Contains the encoded string of the RNA

    #Code to parse the file containing RNA codon encoding and store it in a dictionary
    for line in f:
        temp = line[:-1].split('   ')
        for i in temp:
            if (i==''):
                pass
            else:
                rna_dict[i.split(' ')[0]] = i.split(' ')[1]

    #Code to encode the sequence
    for i in range(0,len(mrna),3):
        if (rna_dict[mrna[i:i+3]] != 'Stop'):
            encoding += rna_dict[mrna[i:i+3]]
        else:
            break
    f.close()
    return print(encoding)


if __name__ == '__main__':
    doctest.testmod(verbose = True)

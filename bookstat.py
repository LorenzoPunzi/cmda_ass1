'''
First assignment of CMEP course: dictionary of characters in a txt file given from command line
'''

import argparse
import time
import matplotlib.pyplot as plt 


def process(file_path):
    '''Opens and reads from input file at file path'''

    #The f is used to use the {} notation->very convenient
    print(f'Opening input file {file_path}...')
    with open(file_path,'r') as input_file:
        text=input_file.read() #reads till end of file
    return text

#Checks whether this module is called as main script from command line
if __name__=='__main__': 

    t0 = time.time()
#Give options to the program when called
    parser = argparse.ArgumentParser(description='Print some book statistics')

#Give an option of string and sets up what --help says for that option
    parser.add_argument('infile', type=str, help='path to the input file')

    parser.add_argument('-hist', action='store_true', help='Display a histogram of occurrences of the characters')
    parser.add_argument('-lim', type=int, default='30', help='Set the number of characters displayed, in descending order of appearance. Default is 30')

#Always do it: it's what you get from command line as option
    args = parser.parse_args()

#Give the function the object given by command line as option infile and assigns it to a str type
    book = process(args.infile)

#create the frequencies dictionary
    freq = {}

    for i in range(len(book)):
        freq[book[i]] = freq.get(book[i],0) + 1
        
    sorted_freq_list = sorted(freq.items(),key = lambda x : x[1], reverse = True)
    freq = dict(sorted_freq_list[:args.lim])
    freq.pop(' ')
    freq.pop('\n')
    if args.hist:
        plt.bar(freq.keys(), freq.values())
    
    print(f'Elapsed time: {time.time()-t0} s')
    #print(freq)
    plt.show()

'''
First assignment of CMEP course
'''

import argparse
import time

def process(file_path):
    '''Opens and reads from input file at file path'''

    #The f is used to use the {} notation->very convenient
        print(f'Opening input file {file_path}...')
        with open(file_path,'r') as input_file:
            text=input_file.read() #reads till end of file

        #print(text)
        #print('Done.')
        return text
        


if __name__=='__main__': #checks whether this module is called as main script from command line

    t0 = time.time()
#gives options to the program when called
    parser = argparse.ArgumentParser(description='Print some book statistics')

#gives an option of string and sets up what --help says for that option
    parser.add_argument('infile', type=str, help='path to the input file')

#always do it: it's what you get from command line as option
    args = parser.parse_args()

#gives the function the object given by command line as option infile
    book = process(args.infile)






    print(f'Elapsed time: {time.time()-t0} s')

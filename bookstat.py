
#First assignment of CMEP course


import argparse



def process(file_path):

	print(f'Opening input file {file_path}...') #The f is used to use the {} notation->very convenient
    with open(file_path,'r') as input_file: #with ensures the file is automatically closed at the end
	    text=input_file.read() #reads till end of file
	print(text)
	print('Done.')


if __name__=='__main__': #checks wether this module is called as main script from command line

	parser = argparse.ArgumentParser(description='Print some book statistics')    #gives options to the program when called
    parser.add_argument('infile', type=str, help='path to the input file')       #gives an option of string and sets up what --help says for that option
    args = parser.parse_args()        #always do it: it's what you get from command line as option
    process(args.infile)              #gives the function the object given by command line as option infile
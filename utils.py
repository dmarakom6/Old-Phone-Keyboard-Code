# basic utilities for encoder and decoder

import sys
import getopt

# gets the input file in command line
def main(argv):
   inputfile = str()
   outputfile = str()
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   return inputfile

import sys
import itertools
from utils import main

decoder_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}



with open(main(sys.argv[1:]), 'r+') as fobj:
   lines = [line for line in fobj]
         
cryp_wds = [cryp_wd.replace('\n', '') for line in lines for cryp_wd in line.split(' ')]
listed_nums = [list(cryp_wd) for cryp_wd in cryp_wds]
   
#removes any invalid character
for a in listed_nums:
    for i in a:
        try:
            int(i)
        except ValueError:
            a.remove(i)

words = []            
for a in listed_nums:    
    letters = []
    l = [(k, sum(1 for _ in v)) for k, v in itertools.groupby(a)] # list of tuples containing the key pressed and how many times it was pressed.
    for t in l: 
        k, v = t[0], t[1]
        letter = decoder_dict[k][v-1]
        letters.append(letter)
    word = ''.join(letters)
    words.append(word)

print('>> ', ' '.join(words))

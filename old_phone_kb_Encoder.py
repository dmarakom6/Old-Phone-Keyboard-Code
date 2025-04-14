import sys
from utils import main
import itertools

encoder_dict = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333',
                'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555',
                'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777',
                's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 
                'x': '99',  'y': '999',  'z': '9999'}


with open(main(sys.argv[1:]), 'r+') as fobj:
   lines = [line for line in fobj]
         
words = [''.join([ch for ch in wd if ch.isalpha()]) for wd in [wd.replace('\n', '') for line in lines for wd in line.split(' ')]]
listed_nums = [[encoder_dict[ch.lower()] for ch in word] for word in words]

# print the message
for i in range(len(listed_nums)):
    listed_nums[i] = ''.join(listed_nums[i])
print('>> ', ' '.join(listed_nums))

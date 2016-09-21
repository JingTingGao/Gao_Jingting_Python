# -*- coding: utf-8 -*-
"""
HW 2

@author: jingtinggao
"""

'''
3. In cryptography, a Caesar cipher is a very simple encryption 
techniques in which each letter in the plain text is replaced 
by a letter some fixed number of positions down the alphabet. 
For example, with a shift of 3, A would be replaced by D, B would 
become E, and so on. The method is named after Julius Caesar, who 
used it to communicate with his generals. ROT-13 ("rotate by 13 places") 
is a widely used example of a Caesar cipher where the shift is 13. 
In Python, the key for ROT-13 may be represented by means of the 
following dictionary:
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
Your task in this exercise is to implement an encoder/decoder of 
ROT-13. Once you're done, you will be able to read the following 
secret message:
   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
Note that since English has 26 characters, your ROT-13 program 
will be able to both encode and decode texts written in English.
'''

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}   # Built a dictionary
def rot_13(code):   
    newcode=''   # Set the initial newcode as none
    for char in code:   # Take every character in the string separately
        if char in key:   # When the character belongs to the dictionary
            newcode+=key[char]   # Add and translate the characgter to newcode
        else:
            newcode+=char   # Otherwise directly add the character to newcode
    return newcode

rot_13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')        
                
'''
7. Using the higher order function reduce(), write a function 
max_in_list() that takes a list of numbers and returns the largest one. 
Then ask yourself: why define and call a new function, when I can just 
as well call the reduce() function directly?   
'''

def max_in_list(lst):
    largest=0   # Set the initial largest to 0
    for i in lst:   # Take every number in the list
        if i>largest:   # Compare the number with current largest
            largest=i   # Replace the largest with larger nuber
    return largest

max_in_list([3,10,8,9,12,5])
       
from functools import reduce   #import reduce function from library
def max_in_list(lst): 
    return reduce(lambda x,y:x if x>y else y, lst)   #return with reduce function
    

max_in_list([3,10,8,9,12,5])
    
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
HW 2
@author: jingtinggao
"""

#Overall Comment: Please refer to Professor G's format, if you have problem with the format, please feel free to email me and
#                 once you  correct the version, I am more than happy to give back your grades. Please understand that the 
#                 meaning of "a list of words" also means one sentense not just {"a", "list", "of", "word"}. If you still have
#                 question about the Q6, I am more than happy to help you with that. And you can discuss those with your friends
#                 come to the office time.
'''
1. Represent a small bilingual lexicon as a Python dictionary in the following 
fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", 
"new":"nytt", "year":"år"} and use it to translate your Christmas cards from 
English into Swedish. That is, write a function translate() that takes a list 
of English words and returns a list of Swedish words.
'''
lexicon={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", 
"new":"nytt", "year":"år"}   # Built a dictionary
def lexicon_dic(inputWord):#define the dictionary that we will use later
    """
    Define a function working as a dictionary
    Parameters:
    inputWord-a string we input
    Returns:
    the translation of the string we input by this dictionary
    """ 
    if inputWord in lexicon_dic:#if the word is in the dictionary, translate it
             return lexicon_dic.get(inputWord)
    else:
             return inputWord
             # if word is not in the dictionary, keep the word
def translate(english):
    """
    Define a function translate your Christmas cards from English into Swedish
    Parameters:
    string-a string we input
    Returns:
    the translation in Swedish
    """ 
    words = string.split( );
    translation = ""#create a new string
    for i in words:
        translation = translation + lexicon_dic(i) + " "
        #use the function we defined early to translate the part that need to 
        #be translated
    return translation
    
translate(["Merry","Christmas","and","Happy","New","Year"])

#Comment: Your logic works for single word, but how about one string? like "Merry Christmas and Happy New Year"?

'''
2. Write a function char_freq()that takes a string and builds a frequency 
listing of the characters contained in it. Represent the requency listing as 
a Python dictionary. Try it with something like 
char_freq("abbabcbdbabdbdbabababcbcbab").  
'''
def char_freq(string):
    """
    Write a function char_freq()that takes a string and builds a
    frequency listing of the characters contained in it. 
    Parameters:
    string-a string we input
    Returns:
    show how many times the each character appears in the string we input
    """
    freq={}   #set the initial frequency as empty set
    for char in string:   #for loop to take each character in the string
        freq[char]=freq.get(char,0)+1   #find the character with .get(i,0)
                                        #add 1 when get a char                               
    return freq

char_freq("abbabcbdbabdbdbabababcbcbab")

'''
3. In cryptography, a Caesar cipher is a very simple encryption techniques in 
which each letter in the plain text is replaced by a letter some fixed number 
of positions down the alphabet. For example, with a shift of 3, A would be 
replaced by D, B would become E, and so on. The method is named after Julius 
Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 
places") is a widely used example of a Caesar cipher where the shift is 13. 
In Python, the key for ROT-13 may be represented by means of the following 
dictionary:
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
Your task in this exercise is to implement an encoder/decoder of ROT-13. Once 
you're done, you will be able to read the following secret message:
   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
Note that since English has 26 characters, your ROT-13 program will be able to 
both encode and decode texts written in English.
'''
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}   # Built a dictionary
def rot_13(code):
    """
    implement an encoder/decoder of ROT-13. Then read the following secret 
    message: Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
    Parameters:
    string-a string we input
    Returns:
    the decoded string
    """ 
    newcode=''   # Set the initial newcode as none
    for char in code:   # For loop taking every character in the string separately
        if char in key:   # if the character belongs to the dictionary
            newcode+=key[char]   # Add and translate the characgter to newcode
        else:
            newcode+=char   # Otherwise directly add the character to newcode
    return newcode

rot_13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')        
 

'''
4. Define a simple "spelling correction" function correct()that takes a string 
and sees to it that 1) two or more occurrences of the space character is 
compressed into one, and 2) inserts an extra space after a period if the 
period is directly followed by a letter. E.g. correct("This is very funny and 
cool.Indeed!")should return "This is very funny and cool. Indeed!" 
'''
import re   # Import reglar expression operation
def correct(string):
    """
    Define a simple "spelling correction" function correct()that takes a
    string and sees to it that 1) two or more occurrences of the space 
    character is compressed into one, and 2) inserts an extra space
    after a period if the period is directly followed by a letter.
    Parameters:
    string-a string we input
    Returns:
    the correction of the string
    """  
    compress=re.sub(' +',' ',string)   # Compress the extra space
    insert=re.sub('\.','. ',compress)   # Insert a space after a period
    correction=insert   #the final correction is equal to insert
    return correction

correct("This is    very funny and cool.Indeed!")     
 

'''
5. The third person singular verb form in English is distinguished by the 
suffix -s, which is added to the stem of the infinitive form: run -> runs. 
A simple set of rules can be given as follows:  a. If the verb ends in y, 
remove it and add ies b. If the verb ends in o, ch, s, sh, x or z, add es c. 
By default just add s  Your task in this exercise is to define a function 
make_3sg_form()which given a verb in infinitive form returns its third person 
singular form. Test your function with words like try, brush, run and fix. 
Note however that the rules must be regarded as heuristic, in the sense that 
you must not expect them to work for all cases. Tip: Check out the string 
method endswith().  
'''
def make_3sg_form(verb):
    """
    define a function make_3sg_form()which given a verb in infinitive
    form returns its third person singular form. 
    Parameters:
    word-a word(verb) we input
    Returns:
    the 3rd perston singular form of the verb
    """
    if verb.endswith('y'):   #if the word end with y
        newverb=verb[:-1]+'ies'   #substract y and add ies
    elif verb.endswith(('o','ch','s','sh','x','z')): #if the word end as listed
        newverb=verb+'es'   #directly add es to the word
    else:
        newverb=verb+'s'   #otherwise directly add s
    return newverb

make_3sg_form('fix')


'''
6. In English, the present participle is formed by adding the suffix -ing to 
the infinite form: go -> going. A simple set of heuristic rules can be given 
as follows:  
a. If the verb ends in e, drop the e and add ing (if not exception: be, see, 
flee, knee, etc.) b. If the verb ends in ie, change ie to y and add ing c. 
For words consisting of consonant-vowel-consonant, double the final letter 
before adding ing d. By default just adding Your task in this exercise is to 
define a function make_ing_form()which given a verb in infinitive form returns 
its present participle form. Test your function with words such as lie, see, 
move and hug. However, you must not expect such simple rules to work for all 
cases.
'''
def make_ing_form(verb):
    """
    Define a function
    make_ing_form()which given a verb in infinitive form returns its
    present participle form.
    Parameters:
    verb-a word(verb) we input
    Returns:
    the present participle form of the verb
    """  
    if verb.endswith('e'):
        presentverb = verb[:-1]+'ing'
        #returns all elements in the string except the last one 'e
        #then add 'ing'
    elif verb.endswith('ie'):
        presentverb = verb.rstrip('ie')+'ying'
        #use rstrip to strip characters from the end of the string
        #then add 'ying'
    elif (verb[-2] in 'aeiou')and(verb[-3] not in 'aeiou')and(verb[-1] not in 'aeiou'):
        #if the word consist of consonant-vowel-consonant
        presentverb = verb+verb[-1]+'ing'
        #double(add) the last letter in the string using[-1]
        #add 'ing'
    else:
        presentverb = verb+'ing'
    return presentverb
make_ing_form('hug')
              
'''
7. Using the higher order function reduce(), write a function 
max_in_list() that takes a list of numbers and returns the largest one. 
Then ask yourself: why define and call a new function, when I can just 
as well call the reduce() function directly?   
'''
       
from functools import reduce   #import reduce function from library
def max_in_list(lst): 
    """
    Using the higher order function reduce(), write a function max_in_list()that
    takes a list of numbers and returns the largest one.
    Parameters:
    list-a list of number we input
    Returns:
    the largest number in the list
    """  
    return reduce(lambda x,y:x if x>y else y, lst) #return with reduce function
    
max_in_list([3,10,8,9,12,5])
    
    
'''
8. Write a program that maps a list of words into a list of integers 
representing the lengths of the correponding words. Write it in three 
different ways: 1) using a for-loop, 2) using the higher order function map(), 
and 3) using list comprehensions.  
'''

# 1) using a for-loop
def word_to_length_one(lst):
    length=[]   #set the initial length with list of empty
    for w in lst:   #for loop take every word in the list
        length.append(len(w))   #add the length of each word to the list
    return length

word_to_length_one (["A", "list", "of", "words"])

# 2) using the higher order function map()
def word_to_length_two(lst):
    return list(map(len,lst))   
    #map each word in the list with length function and list them
    
word_to_length_two (["A", "list", "of", "words"])

# 3) using list comprehensions
def word_to_length_three(lst):
    return [len(w) for w in lst]   #return the list of length for each word

word_to_length_three (["A", "list", "of", "words"])


'''
9. Write a function find_longest_word()that takes a list of words and returns 
the length of the longest one. Use only higher order functions.  
'''
def find_longest_word(lst):
    """
    Write a function find_longest_word()that takes a list of words
    and returns the length of the longest one. Use only higher order
    functions. 
    Parameters:
    string-a string we input
    Returns:
    the longest word in the list
    """ 
    return max(list(map(len,lst)))
    #apply map function to get each length of word in the list and find the 
    #maximum in the list

find_longest_word(['find','the','longest','word','please'])

'''
10. Using the higher order function filter(), define a function 
filter_long_words()that takes a list of words and an integer n and returns the 
list of words that are longer than n.  
'''
def filter_long_words(lst,n):
    """
    Write a function filter_long_words()that takes a list of words and an integer 
    n and returns the list of words that are longer than n.
    arameters:
    list-a list of word we input
    n-a number we input
    Returns:
    a new list that filtered the word in the list we input longer than 'n'
    """
    return list(filter(lambda x:len(x)>n,lst))
    #apply filter to get all the inputs satisfies the condition that 
    #length is greater than n
    
filter_long_words(['how','to','filter','long','words'],3)    

'''
11. Represent a small bilingual lexicon as a Python dictionary in the 
following fashion {"merry":"god", "christmas":"jul","and":"och","happy":"gott",
"new":"nytt","year":"år"}and use it to translate your Christmas cards from 
English into Swedish. Use the higher order function map()to write a function 
translate() that takes a list of English words and returns a list of Swedish 
words.  
'''
lexicon={"merry":"god", "christmas":"jul","and":"och","happy":"gott",
"new":"nytt","year":"år"}

def translate(english):
    """
    Use the higher order function map()to write
    a function translate() that takes a list of English words and
    returns a list of Swedish words. 
    Parameters:
    inputWords-a list of word we input
    Returns:
    the Swedish translation of the list 
    """ 
    return list(map(lambda x:lexicon[x.lower()],english))
    #list the result of translation which is mapped from english word to 
    #corresponding swidsh word

translate(["Merry","Christmas","and","Happy","New","Year"])


'''
12. Implement the higher order functions map(), filter()and reduce(). 
(They are built-in but writing them yourself may be a good exercise.)    
''' 
 # map()
def map_func(function, iterable):
    """
    Defining a function work as filter function 
    Parameters: 
    function-a function we defined
    list-a list of number we input
    Return: filter the number in the list which do not satisfy the function we defined
    """    
    mresult=[]
    for i in iterable:   #for loop take every i in iterable
        mresult.append((funtion(i))   #apply function to each i in iterable 
    return mresult                    #in order to get result
  
#filter()
def filter_func(function, iterable):
"""
    Defining a function work as filter function 
    Parameters: 
    function-a function we defined
    list-a list of number we input
    Return: filter the number in the list which do not satisfy the function we defined
    """    
    fresult=[]
    for i in iterable:   #for loop take every i in iterable
        if function(i)==True:   #if the item is trun under the function
            fresult.append(i)   #add the item to the result
    return fresult
    
#reduce()
def reduce_func(function, sequence,initial=None):
    """
    Defining a function work as reduce function 
    Parameters: 
    function-a function we defined
    list-a list of number we input
    Return: reduce the number in the list that satisfy the function we defined
    """
    rresult=initial if initial else esquence[0]   #the result is initial value
    for i in wequence:   #for loop take each element in sequence
        rresult=function(rresult,i)   #apply the function to the initial result
    return rresult
    
    
    
    
    
    

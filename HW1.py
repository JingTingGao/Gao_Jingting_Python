# -*- coding: utf-8 -*-
"""
Gao_JingTing
HW1
"""
#Overall Comment: Good start. But please refer to the format that Prof.G has shown you during the class to correct your own 
#format. If you wish, you can correct this and you will have your mark back. And for the code, please try to includes all possible
#situations. You can see my comment as "Comment:   ", if any misunderstanding happened, please feel free to email me.
'''
1. Define a function max() that takes two numbers as arguments 
and returns the largest of them. Use the if-then-else construct 
available in Python. (It is true that Python has the max() function 
  built in, but writing it yourself is nevertheless a good exercise.)
'''

def print_max(a, b):   
     if a >= b:   #comparing a and b     
         print(a,' is maximum')   
     else:       
         print(b,' is maximum')

print_max(2,3) 

'''
2. Define a function max_of_three() that takes three 
numbers as arguments and returns the largest of them.
'''
def max_of_three(a, b, c):
    if a >= b:   #comparing a and b if a>=b
        if a >= c:   #comparing a and c
            print(a, ' is maximum')
        else: 
            print(c, ' is maximum')   
    else:   #else if b>=a 
        if b >= c:   #comparing b and c       
           print(b, ' is maximum') 
        else: 
           print(c, ' is maximum')

max_of_three(3, 5, 10)

'''
3. Define a function that computes the length of a 
given list or string. (It is true that Python has 
the len() function built in, but writing it yourself 
is nevertheless a good exercise.)
'''
def length(string):
    c=0   #set the initial count as 0
    for i in string: #for each letter in the list or string count+1
        c+=1
    return c

length('stupid ')

'''
4.Write a function that takes a character (i.e. a 
string of length 1) and returns True if it is a vowel, 
False otherwise.
'''
vowels=['a','i','u','e','o']   #set a set of vowels

def v(char):
    if char in vowels:   #if statement to check if the character is a vowel
        return True
    return False
        
v('e')     
v('p')   
#Comment: Think about the capital letters. Try to cover all possible situations.
'''
5. Write a function translate()that will translate a text 
into "rövarspråket" (Swedish for "robber's language"). 
That is, double every consonant and place an occurrence 
of "o"in between. For example, translate("this is fun") 
should return the string"tothohisosisosfofunon".  
'''

vowels=['a','i','u','e','o',' ']   #a set of everything do not need to change
#Comment: why include a empty space? Also, cover the capital letters.
def translate(string):
    result=''   #set the initial result
    for l in string:
        if l in vowels:   #for elements not necessary to change just add on
            result+=l
        else:   #translate consonants which are not belong to set of vowels 
            result+=l+'o'+l
    return result
    
translate('python is so hard')

'''
6. Define a function sum() and a function multiply() that 
sums and multiplies (respectively) all the numbers in a list 
of numbers. For example, sum([1, 2, 3, 4]) should return 10, 
and multiply([1, 2, 3, 4]) should return 24.
'''

def sum(lst):
    s=0   #set the initial sum as 0
    for i in lst:   #add on each number in the list
        s+=i
    return s

sum([1,2,3,4])

def multiply(lst):
    m=1   #set the initial multiply as 1
    for i in lst:   #multiply each number to m
        m*=i
    return m
    
multiply([1,2,3,4])

'''
7. Define a function reverse() that computes the reversal 
of a string. For example, reverse("I am testing") should 
return the string "gnitset ma I".
'''

def reverse(string):
    return string[::-1]   #from the 1st character to the last written backward
    
reverse("I am testing")

'''
8. Define a function is_palindrome() that recognizes 
palindromes (i.e. words that look the same written backwards). 
For example, is_palindrome("radar") should return True.
'''

def is_palindrome(string):
  string=string.upper()   #set upper letter same as lower
  string=string.replace(" ","")   #eliminate the influence of space
  return string == string[::-1]   #check if the string equals to the reverse 
     

is_palindrome("radar")
is_palindrome("sb")

'''
9. Write a function is_member() that takes a value 
i.e. a number, string, etc) x and a list of values a, 
and returns True if x is a member of a, False otherwise. 
(Note that this is exactly what the in operator does, but 
  for the sake of the exercise you should pretend Python 
  did not have this operator.)
'''

def is_member(x, lst):
    for a in lst:
        if x==a:   #check if x equals to any element in the list 
            return True
    return False

is_member('a',['aaa','abd','c',1])
is_member('b',['g','e'])
#Comment: You can improve the logic with 'in' which is a logic judge.
'''
10. Define a function overlapping() that takes two lists and 
returns True if they have at least one member in common, 
False otherwise. You may use your is_member() function, 
or the in operator, but for the sake of the exercise, 
you should (also) write it using two nested for-loops.
'''

def overlapping(lst1, lst2):
    for i in lst1:   #take an element i from list1
      for j in lst2:   #take an element j from list2
        if i==j:   #check if any i equals j
            return True
    return False
        
overlapping(['a','c','f','e','h'],['e','h','s','t'])
overlapping(['nope', 'nothing', 'in'], ['common'])
overlapping(['this', 'might', 'work'], ['or', 'maybe', 'this'])

'''
11. Define a function generate_n_chars() that takes an 
integer n and a character c and returns a string, n 
characters long, consisting only of c:s. For example, 
generate_n_chars(5,"x") should return the string "xxxxx". 
(Python is unusual in that you can actually write an expression 5 * "x" 
that will evaluate to "xxxxx". For the sake of the exercise you should 
ignore that the problem can be solved in this manner.)
'''

def generate_n_chars(n,c):
    result=""   #set the initial result
    for i in range(n):   #for in loop to add the character n times
        result+=c
    return result
    
generate_n_chars(5,'a')
generate_n_chars(10,'hi')

'''
12. Define a procedure histogram() that takes a list of 
integers and prints a histogram to the screen. For example, 
histogram([4, 9, 7]) should print the following:
**** ********* *******
'''

def histogram(lst):
    for i in lst:   #take each integer i from the list
        print(i*'*')   #return i times of * for each i
        
histogram([4,9,7])

'''
13. The function max() from exercise 1) and the function 
max_of_three() from exercise 2) will only work for two 
and three numbers, respectively. But suppose we have a 
much larger number of numbers, or suppose we cannot tell 
in advance how many they are? Write a function max_in_list() 
that takes a list of numbers and returns the largest one.
'''

def max_in_list(lst):
    max=0   #set the initial max as o
    for i in lst:   #for loop to take every number in the list
        if i>max:   #if any number in the list is greater than max
            max=i   #replace max with the number
    return max

max_in_list([3,6,1,78,45,35,1])

'''
14. Write a program that maps a list of words into a list 
of integers representing the lengths of the correponding words.
'''

def length_of_words(lst):
    l=0   #set the initial length of word l as 0
    for w in lst:   #for loop to take every word from the list
        l+=len(w)   #add all the length of all words in the list
    return l

length_of_words(['python','is','odd'])

'''
15. Write a function find_longest_word() that takes 
a list of words and returns the length of the longest one.
'''

def find_longest_word(lst):
    longest=''   #set the initial longest word as none
    for w in lst:   #for loop to take every word from the list
        if len(w)>len(longest): #if any word is longer than the current longest
            longest=w   #replace the longest with the word
    return len(longest) #return the length of final longest word
    
find_longest_word(['python','is','interesting'])

'''
16. Write a function filter_long_words() that takes a list 
of words and an integer n and returns the list of words that 
are longer than n.
'''            

def filter_long_words(lst, n):
  return [w for w in lst if len(w) > n] 
  #return all the words from list whose lengh is bigger than input integer n
  
filter_long_words(['python','is','kind','of','fun','after','learning'],5)


































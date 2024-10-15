import string

def is_palindrome(string):
  
    string_ = ''.join(letter.lower() for letter in string if letter.isalnum()) # remove all spaces and convert all to lowercase
    
    stack = [] # create an empty list
  
    for letter in string_:
        stack.append(letter) # put all the characters into the string 
      
    for letter in string_:
        if letter != stack.pop(): # compare if the characters match the requirement
            return False # if not, then it is false
    
    return True # if all match, then it is true.

# all example
print(is_palindrome('radar')) #True
print(is_palindrome('Mom')) #True
print(is_palindrome('civic')) #True
print(is_palindrome('hello')) #False
print(is_palindrome('my name is Thy')) #False

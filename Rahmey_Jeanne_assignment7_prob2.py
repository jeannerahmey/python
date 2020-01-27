#Jeanne Rahmey
#CSCI-2
#Ass. 7
#Prob 2 a, b


#Prob 2A

import random

def add_letters (word, num):
    # function:   add_letters
    # input:      a word to scramble (String) and a number of letters (integer)
    # processing: adds a number of random letters (A-Z; a-z) after each letter
    #in the supplied word
    #output: returns new word
    '''
    (str, int) -> str
    '''
    new = ''
    for c in word:
    #(65 , 90) --> uppercase letters
    #(97, 122) --> lowercase letters
        new += c
        for i in range (num):
            while True:
                rand = random.randint(65, 122)
                if rand > 57 and rand < 65:
                    rand = random.randint(65, 122)
                else:
                    new += chr(rand)
                    break
    return new

#print(add_letters ('cat', 2))


def remove_letters (word, num):
    #input: word (str), characters to remove(int)
    #processing:the function starts at the first position in the supplied word
    #and keeps it. it then removes "num" characters from the word.
    #the process is repeated again
    #output: returns newly unscrambled word
    '''
    (str, int) --> str
    '''
    new = word[0:len(word): num+1]
    return new

'''
word1 = "HdeulHlHom!t"
word2 = "HTLedklFNljioMH!bi"
word3 = "HHHZeZrflqSflzOiosNU!jBk"
word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"
unscrambled1 = remove_letters(word1, 1)
print ("Removing 1 characer from", word1, "->", unscrambled1)
unscrambled2 = remove_letters(word2, 2)
print ("Removing 2 characers from", word2, "->", unscrambled2)
unscrambled3 = remove_letters(word3, 3)
print ("Removing 3 characers from", word3, "->", unscrambled3)
'''


def shift_characters(word, num):
    #function: shift_characters
    #input: a word (String) and a number of characters to shift (integer)
    #processing: shifts each character in the supplied word to another position
    #in the ASCII table. the new position is dictated by the supplied integer.
    #output: returns newly generated word
    '''
    (str, int)-->str
    '''
    new = ""
    for i in (word):
        letter =chr((ord(i) + num) % 128) 
        new+=letter
    return new

'''
word1 = "apple"
newword1 = shift_characters(word1, 1)
print (word1, "shifted by +1 is", newword1)
        
word2 = "Pears are yummy!"
newword2 = shift_characters(word2, 2)
print (word2, "shifted by +2 is", newword2)
unscrambled2 = shift_characters(newword2, -2)
print (newword2, "shifted by -2 is", unscrambled2)
'''


###################################
#Prob 2B

while True:
    option = input("encode, decode, or quit?: ")
    new_phrase = ''
    shifted_phrase = ''
    if option == "encode":
        while True:
            num = int(input("Enter number between 1 and 5: "))
            if num < 1 or num > 5:
                print("Invalid number, try again.")
            else:
                break
        phrase = input("Enter phrase to encode: ")
        shifted_phrase += shift_characters(phrase, num)
        new_phrase += add_letters(shifted_phrase, num)
        
        print("Your encoded word is:", new_phrase)
    elif option == "decode":
        while True:
            num = int(input("Enter number between 1 and 5: "))
            if num < 1 or num > 5:
                print("Invalid number, try again.")
            else:
                break
        phrase = input("Enter phrase to decode: ")
        shifted_phrase += shift_characters(phrase, (num * -1))
        new_phrase += remove_letters(shifted_phrase, num)
            
        print("Your decoded word is:", new_phrase)
    else:
        break












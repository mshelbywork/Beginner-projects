#generate text anaylzer

#for loop

#count total words, vowels and specific character appearance

#at least one function

'''user input>for loop | interate variable> print result
bonus: let user choose, one function per analysis type, ignore
punctuation, make counting case-insensitive
'''
print('This program can take the data you input to count total words, count total vowels, or \n search how often a letter appears ')
stuff = input ('Please input data: ')
print (stuff)

def total_word ():
    seperate = stuff.split(' ')
    for index, words in enumerate(seperate, 0):
        pass
        print (index, words)




def vowels():
    count = 0
    for letter in stuff:
        if letter == 'a':
            count += 1
        if letter == 'e':
            count += 1
        if letter == 'i':
            count += 1
        if letter == 'o':
            count += 1
        if letter == 'u':
            count += 1
    print(count)
#count how many times a specific letter appears, based on input?

def count_check():
    word_check=[]
    for words in stuff:
        word_check.append(words)
    CCV = input('search how many times a letter appears: ') #check count variable 

    print(f'Instances of {CCV} =', word_check.count(CCV))
def main():
    print ('-please select number from the options below-')
    print ('1. count total words')
    print ('2. Count vowels')
    print ('3. count specific letter')
    
    selection = int(input (''))

    if selection == 1:
        total_word()
    if selection == 2:
        vowels()
    if selection == 3:
        count_check()
    if selection != 1 or selection != 2 or selection != 3:
        print ('please select from list')
main ()




'''
print ('- make a selection -')
print ('1. Count total words')
print ('2. Count vowels')
print ('3. Count how many times a specific letter appears')
user_in= int(input (''))

'''
#if elif else:?
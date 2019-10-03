"""
Write a function to change every second word in a sentence to "Hello"

Example 
sentence = Hey I love going to the park 
         ==> Hey Hello love Hello to Hello park

"""

def sentenceReplace(sentence):
    #declaring a string to keep all the words after each loop and index as a counter
    new_sentence = ""
    index = 0
    #start looping through every word to check which are 'every second word in the sentence'
    for word in sentence.split():
        if index % 2 == 1:
            new_sentence += " Hello "
        else:
            new_sentence += word
        index += 1
    #remove last space from sentence (as it is " Hello " being added each time) and print
    sentence = sentence[:-1]
    print(new_sentence)

#execute the function
sentenceReplace(input("Enter Your Sentence: "))
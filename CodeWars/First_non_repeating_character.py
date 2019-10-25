def first_non_repeating_letter(string):
    """
    This was created for Code Wars:
    https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
    
    This function takes a string as an input.
    It will return the first character the does not repeat in the string.
    It is case insensitive
    """    
    
    #checks for empty string
    if string == "":
        return ""
    else:
        
        #creates list which will check if there is a repeated character
        list = []
        
        #iterates through string to count how many times it appears
        #keeps track of occurences by adding counts to list
        for i in string:
            list.append(string.lower().count(i.lower()))
            if string.lower().count(i.lower()) > 1:
                pass
            else:
                return i           
                #break so only first occurence is taken
                break
                
        #if no character occured only a single time, a blank string will be return
        if 1 not in list:
            return ""
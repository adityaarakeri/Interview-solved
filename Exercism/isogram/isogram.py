def is_isogram(string):
    string = string.upper()
    for letter in string:
        if(letter.isalpha() and string.count(letter) > 1):
            return False
    return True
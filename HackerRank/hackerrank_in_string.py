"""
https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
"""
def hackerrankInString(s):
    word = 'hackerrank'
    count = 0
    if word == s:
        return 'YES'
    if s == '' or len(s) < len(word) or len(s) > 10**4:
        return 'NO'
    else:
        for i,e in enumerate(word):
            index = s.find(e)
            if index == -1:
                return 'NO'
            else:
                s = s[index+1:]
                continue
        return 'YES'
            
        
if __name__ == '__main__':

    s = raw_input()


    result = hackerrankInString(s)
    print (result)
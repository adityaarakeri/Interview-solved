"""
URL:
https://www.codewars.com/kata/54da539698b8a2ad76000228

DESCRIPTION: 
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, 
so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, 
so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. 
Return false otherwise.
"""

def isValidWalk(walk):
    if len(walk) != 10:
        return False
    
    d = {
        "n": 0,
        "s": 0,
        "e": 0,
        "w": 0
    }
    for elem in walk:
        if elem in d.keys():
            d[elem] += 1
    
    return (d["n"] == d["s"]) and (d["e"] == d["w"])
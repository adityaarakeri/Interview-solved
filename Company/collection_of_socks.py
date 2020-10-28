"""
If your sock drawer has 6 black socks, 4 brown socks, 8 white socks, and 2 tan socks, how many socks would you have to pull out in the dark to be sure you had a matching pair?

"""

# Data
collection = {
    'black': 6,
    'brown': 4,
    'white': 8,
    'tan': 2
}


def choose_random(collection, picks=1):

    box_of_socks = []
    for i in range(len(collection)):
        box_of_socks.append([str(collection.keys()[i])]
                            * collection.values()[i])

    choice = []
    for color_box in box_of_socks:
        if len(color_box) > 0:
            pick = color_box.pop()
            if pick in choice:
                break
            else:
                choice.append(pick)

    return len(choice)+1


print(choose_random(collection, picks=1))

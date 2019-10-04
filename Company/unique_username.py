"""
Unique usernames
You get an list of names and need to return a list of unique usernames.
For a duplicate name, add the next integer after the name

For example:

Input
['Julie', 'Emma', 'Zoe', 'Liam', 'Emma']
Output
['Julie', 'Emma', 'Zoe', 'Liam', 'Emma1']

Input
['Julie', 'Zoe', 'Zoe', 'Liam', 'Emma', 'Zoe']
Output
['Julie', 'Zoe', 'Zoe1', 'Liam', 'Emma', 'Zoe2']
"""


def users(names):
    usernames = []
    for name in names[1:]:
        if name not in usernames:
            usernames.append(name)
        else:
            count = sum(name in user for user in usernames)
            usernames.append(name + str(count))

    return usernames



By using Python <tuple()> function we can convert a list into a tuple. But we can’t change the list after turning it into tuple, because it becomers immutable.

Example:

weekdays = [‘sun’,’mon’,’tue’,’wed’,’thu’,’fri’,’sat’]
listAsTuple = tuple(weekdays)
print(listAsTuple)

output: (‘sun’, ‘mon’, ‘tue’, ‘wed’, ‘thu’, ‘fri’, ‘sat’)

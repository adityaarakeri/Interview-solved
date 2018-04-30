from ImplementQueue import Queue

def hotPotato(lst, num):

    queue = Queue()

    for item in lst:
        queue.enqueue(item)


    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()


lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print hotPotato(lst, 7)

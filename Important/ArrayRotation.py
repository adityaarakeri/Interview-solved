# Rotate the array Left and Right

# rotate the array to left i.e move along in <----
def rotateLeft(array, rotations):

    # if array==[] or rotations==0:
    #     return array
    #
    # return array[rotations:]+array[:rotations]

    # returning the array if the no of rotations is a multiple of len(array)
    if rotations % len(array) == 0:
        return array

    r_array = [0]*len(array)

    for i, e in enumerate(array):
        ind = (i-rotations) % len(array)
        r_array[ind] = e

    return r_array


# rotate the array to right i.e move along in ---->
def rotateRight(array, rotations):

    # returning the array if the no of rotations is a multiple of len(array)
    if rotations % len(array) == 0:
        return array

    r_array = [0]*len(array)

    for i, e in enumerate(array):
        ind = (i+rotations) % len(array)
        r_array[ind] = e

    return r_array


array = map(int, input(
    'enter the values of the array with a space in between > ').strip().split(' '))
rotations = int(input('enter the no of rotations > ').strip())
print(rotateLeft(array, rotations))
print(rotateRight(array, rotations))

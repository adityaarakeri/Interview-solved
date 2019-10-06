#This question was asked by Amazon in 1st Round of Technical Interview 
'''
Question : You are given a playlist of music and you have to do a perfect shuffling of songs such that no song remains at its original positon

Solution : There is a famous algorithm of shuffling a given array of integers - known as Fisher-Yeats Shiffling Algorithm.

Map each song to a number equal to index of array integers in the array and run this algorithm to shuffle the index and then to play a particular song
, just print the value of that index of music to play the song in the playlist
'''
import random 
  
def play_music_order(arr):
    for i in arr:
        print(music_playlist[i])
# A function to generate a random permutation of arr[] 
def randomize (arr, n): 
    # Start from the last element and swap one by one. We don't 
    # need to run for the first element that's why i > 0 
    for i in range(n-1,0,-1): 
        # Pick a random index from 0 to i 
        j = random.randint(0,i+1) 
  
        # Swap arr[i] with the element at random index 
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 
  
# Driver program to test above function. 
music_playlist={
    1:"Closer",
    2:"The Night We Met",
    3:"Passenger-Let Her Go",
    4:"Simple Song",
    5:"Afreen-Afreen",
    6:"Tune Jo Na Kaha",
    7:"Love Yourself",
    8:"Baby-2",
}

arr = [1, 2, 3, 4, 5, 6, 7, 8] 
play_music_order(arr)
n = len(arr) 
new_arr=randomize(arr, n)
print("")
print("Shuffled Playlist:")
print("")
play_music_order(new_arr)
'''
You are given an array of integers, and you have to find the k-th smallest number in the array.

Input Format:

The first line contains the value of K
The second line contains a space separated list of integers


Output Format:

The only line contains the k-th smallest number in the array

'''

k = int(input("Enter K: "))
print("Enter the array: ")
arr = list(map(int, input().split(" ")))

arrNew = sorted(arr)

for i in range(1, k):
    del arrNew[0]
print(arrNew[0])

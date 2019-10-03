k = int(input("Enter K: "))
print("Enter the array: ")
arr = list(map(int, input().split(" ")))

arrNew = sorted(arr)

for i in range(1, k):
    del arrNew[0]
print(arrNew[0])
# Python Program / Project

def SaddlePoint(arr, n):
    col = flag = 0
    for i in range(0, n):
        minVal = arr[i][0]
        for j in range(0, n):
            if (minVal > arr[i][j]):
                minVal = arr[i][j]
                col = j
        maxVal = arr[i][col]
    
    for i in range(0, n):
        for j in range(0, n):
            if maxVal < arr[i][col]:
                maxVal = arr [i][col]
    
    if (minVal == maxVal):
        print("Saddle point Fund: ")
        flag = 1
        print("Number is : %d" % maxVal)

    if flag == 0:
        print("No Saddle point Found in Array.")

# Driver code
print("********** Saddle Point Demo **********")
n = int(input("Enter the order of the matrix: "))
arr = [[0 for col in range(n)] for row in range(n)]

for row in range(0, n):
    for col in range(0, n):
        item = int(input("Enter the element: "))
        arr[row][col] = item

print("\nYou have entered following matrix: ")
for row in range(0, n):
    for col in range(0, n):
        print(arr[row][col], end=" ")
    print()

SaddlePoint(arr, n)
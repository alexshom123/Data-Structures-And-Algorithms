#Array/List practice problems
import numpy as np

#1 - find missing number in sequence (I used sequence sum formula 1+2+3...+n = n(n+1)/2)
sequence = [1,2,3,4,6,7,8,9,10]

def findMissing(list):
    n = len(list) + 1
    sum1 = ((n*(n+1))/2)
    sum2 = sum(list)
    return sum1 - sum2

print(f"The missing number in the sequence is {findMissing(sequence)}\n")

#2 - find all pairs in an array which sum to a specific number in the array
myList = [1,2,3,4,5,6,7,8,9,10]

def pairs(list, sum):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if ((list[i] + list[j]) == sum):
                print(list[i], list[j])

print("The pairs in myList that sum to 10 are: \n") 
pairs(myList, 10)
print("\n")

#3 - find max product between two integers of an array if all array elements are positive
myArray = np.array([1,5,6,10,12,7])

def maxProduct(array):
    maximum = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            product = array[i]*array[j]
            if (product > maximum):
                maximum = product
    return maximum

print(f"The maxium product in myArray is {maxProduct(myArray)}\n")

#4 - determine if all elements in a list are unique
aList = [1,2,3,4,5,5,6,7,8,9,10,5,11,11]

def unique(list):
    checked = []
    repeated = []
    for i in range(len(list)):
        if list[i] not in checked:
            checked.append(list[i])
        else:
            if list[i] not in repeated:
                repeated.append(list[i])
    if repeated:
        print(f"All the values in the array are not unique as the elements {repeated} are repeated.")
    else:
        print("All elements are unique.")

unique(aList)

#5 - Rotate matrix/array by 90 degrees
npArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

def rotate(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            #save top element
            top = matrix[layer][i]
            #move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            #move bottom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            #move right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            #move top to right
            matrix[i][-layer-1] = top
    return matrix

print(f"The original matrix \n{npArray}\n roated by 90 degress is \n{rotate(npArray)}\n")
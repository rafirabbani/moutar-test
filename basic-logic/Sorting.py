def merge(leftList, rightList):
    sortedList = []
    leftListIndex = rightListIndex = 0

    # Assign both lists length into variables
    leftListLength, rightListLength = len(leftList), len(rightList)
    
    for _ in range(leftListLength + rightListLength):

        #Check index of both left and right lists
        if leftListIndex < leftListLength and rightListIndex < rightListLength:

            #Check which list have lower value on the first index
            #If leftList has lower value on the first index, add into sortedList
            if leftList[leftListIndex] <= rightList[rightListIndex]:
                sortedList.append(leftList[leftListIndex])
                leftListIndex += 1
            
            #If rightList has lower value on the first index, add into sortedList
            else:
                sortedList.append(rightList[rightListIndex])
                rightListIndex += 1
        
        #If all elements of leftList are added, add the elements
        #from the rightList
        elif leftListIndex == leftListLength: 
            sortedList.append(rightList[rightListIndex])
            rightListIndex += 1
        
        #If all elements of rightList are added, add the elements
        #from the leftList
        elif rightListIndex == rightListLength:
            sortedList.append(leftList[leftListIndex])
            leftListIndex += 1

    return sortedList


def mergeSort(nums):
    #If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    #Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    #Sort and merge each half
    leftList = mergeSort(nums[:mid])
    rightList = mergeSort(nums[mid:])
    
    #Merging both lists into new list
    return merge(leftList, rightList)

#Test Code
numsList = [10,5,2,1,8,9,3,0]
print(mergeSort(numsList))
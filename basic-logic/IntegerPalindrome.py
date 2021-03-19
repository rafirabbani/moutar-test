#Function

def intPalindrome(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0 :
            if str(arr[i]) == str(arr[i])[::-1]:
                count += 1
    print(count)

#Test Code
   
intPalindrome([202,101,222,32,154])
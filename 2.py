
def find_largest(arr):
    largest = arr[0] 
    for num in arr:
        if num > largest:
            largest = num
    return largest

# Examples
print(find_largest([1, 8, 7, 56, 90]))  
print(find_largest([5, 5, 5, 5]))      
print(find_largest([10]))             


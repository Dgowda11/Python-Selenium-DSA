def merge(lst1,lst2):
    combined = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            combined.append(lst1[i])
            i += 1
        else:
            combined.append(lst2[j])
            j += 1
    while i < len(lst1):
        combined.append(lst1[i])
        i += 1
    while j < len(lst2):
        combined.append(lst2[j])
        j += 1
    return combined

print(merge([1,2,7,8],[3,4,5,6]))

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid_Index = int(len(lst)/2)
    # Here we are calling the recusive fuction to break the list again and again
    left = merge_sort(lst[:mid_Index])
    right = merge_sort(lst[mid_Index:])
    return merge(left,right)

# Call the Complete Merge Function here
print(merge_sort([3,2,4,1]))
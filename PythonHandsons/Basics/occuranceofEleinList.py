
lst = [2,4,6,2,2,12,4,16,5]
# count = lst.count(2)
repeated_Elements = []
count = 0

for element in set(lst):
    count = lst.count(element)  # Count occurrences of the element
    if count > 1:  # Only add if repeated
        repeated_Elements.append(f"Element: {element}, Repeated_Count: {count}")

# Print the result
print(repeated_Elements)
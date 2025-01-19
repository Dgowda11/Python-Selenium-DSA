# Find non repeating character
s = 'swiss'
def non_repating(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

print(non_repating('Darshan'))

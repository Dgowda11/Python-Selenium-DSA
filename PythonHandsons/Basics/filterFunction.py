# Function that filters Vowels
def fun(varibles):
    letter = ['a','e','i','o','u']
    if varibles in letter:
        return True
    else:
        return False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = filter(fun,sequence)

print("Filtered Letters are :")
for s in filtered:
    print(s)
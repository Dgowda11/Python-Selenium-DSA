str = "Welcome to Python Programming"
sub_str = input("Enter the word :")
str = str.lower()

if(str.find(sub_str)) == -1:
    print("Not Found")
else:
    print("Found")
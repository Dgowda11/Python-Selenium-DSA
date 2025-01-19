


x = 'awesome'

def myfunc():
    global x   # You can make it Global using the Global Keyword here
    x = "fantastic"
    print("Python is "+x)

myfunc()
print(x)


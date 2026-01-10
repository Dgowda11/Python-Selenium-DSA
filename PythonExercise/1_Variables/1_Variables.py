x = [1,2,3]
y =x
y.append(4)
print(x)



# Python decides variable scope at compile time, not runtime.
count = 10
def inc(count):
    return count + 1

print(inc(count))

